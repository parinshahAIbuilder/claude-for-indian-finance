#!/usr/bin/env python
"""Inventory an annual report folder and extract everything to text.

    python probe.py <directory> [--out DIR]

Reports every PDF, Excel workbook and Word document with size, modification
date, page or sheet count; flags likely superseded versions; extracts each file
to text in the output directory; and runs the staleness checks that decide what
you are entitled to conclude from the working papers.
"""
import argparse, os, re, sys, zipfile
from datetime import datetime

sys.stdout.reconfigure(encoding="utf-8", errors="replace")


def human(n):
    return f"{n/1024/1024:.1f} MB" if n > 1024 * 1024 else f"{n/1024:.0f} KB"


def stem(name):
    """Strip version decoration so sibling versions group together."""
    s = os.path.splitext(name)[0]
    s = re.sub(r"[\s_\-]*\(?\d{1,2}[\.\-_]?\d{0,2}[\.\-_]?20\d{2}\)?", "", s)
    s = re.sub(r"[\s_\-]*\(\d+\)", "", s)
    s = re.sub(r"[\s_\-]*(final set|final|v\d+|_\d{3,4})\b", "", s, flags=re.I)
    return re.sub(r"\s+", " ", s).strip().lower()


def do_pdf(path, out):
    import pdfplumber
    base = os.path.splitext(os.path.basename(path))[0]
    txt = os.path.join(out, f"{base}.txt")
    n, chars = 0, 0
    with pdfplumber.open(path) as pdf:
        n = len(pdf.pages)
        with open(txt, "w", encoding="utf-8") as f:
            for i, p in enumerate(pdf.pages, 1):
                f.write(f"\n\n########## PAGE {i} ##########\n")
                t = p.extract_text(layout=True) or ""
                chars += len(t)
                f.write(t)
    flag = "  SCANNED OR VECTOR, render to read" if n and chars / n < 300 else ""
    return f"{n} pages", txt, flag


def do_xlsx(path, out):
    import openpyxl
    base = os.path.splitext(os.path.basename(path))[0]
    wb = openpyxl.load_workbook(path, data_only=True, read_only=True)
    sheets = wb.sheetnames
    wb.close()
    # staleness + integrity probe on the full (non read-only) object
    wb = openpyxl.load_workbook(path, data_only=True)
    cur = prior = refs = notes = 0
    pat_note = re.compile(r"to be (confirm|updated|discuss|check|received)|pending|not done|"
                          r"to confirm|restate to confirm|not mentioned in report", re.I)
    for sn in sheets[:60]:
        ws = wb[sn]
        for row in ws.iter_rows(min_row=1, max_row=min(ws.max_row, 250),
                                max_col=min(ws.max_column, 14), values_only=True):
            for v in row:
                if v is None:
                    continue
                s = str(v)
                if s.startswith("#") and s.rstrip("!") in ("#REF", "#VALUE", "#DIV/0", "#N/A", "#NAME?"):
                    refs += 1
                elif pat_note.search(s):
                    notes += 1
    wb.close()
    parts = len(zipfile.ZipFile(path).namelist())
    flag = ""
    if refs:
        flag += f"  {refs} formula errors"
    if notes:
        flag += f"  {notes} open preparer notes"
    return f"{len(sheets)} sheets, {parts} parts", None, flag


def do_docx(path, out):
    from xml.etree import ElementTree as ET
    W = "{http://schemas.openxmlformats.org/wordprocessingml/2006/main}"
    base = os.path.splitext(os.path.basename(path))[0]
    txt = os.path.join(out, f"{base}.txt")
    z = zipfile.ZipFile(path)
    root = ET.fromstring(z.read("word/document.xml"))
    lines = []
    for el in root.iter():
        if el.tag == W + "p":
            t = "".join(n.text or "" for n in el.iter(W + "t")).strip()
            lines.append(t)
    open(txt, "w", encoding="utf-8").write("\n".join(lines))
    flag = ""
    names = z.namelist()
    d = z.read("word/document.xml").decode("utf-8", "ignore")
    if "word/comments.xml" in names:
        cr = ET.fromstring(z.read("word/comments.xml"))
        c = len(cr.findall(W + "comment"))
        if c:
            flag += f"  {c} UNRESOLVED COMMENTS"
    if "<w:ins " in d or "<w:del " in d:
        flag += "  TRACKED CHANGES PRESENT"
    try:
        core = z.read("docProps/core.xml").decode("utf-8", "ignore")
        lm = re.search(r"lastModifiedBy>([^<]*)<", core)
        md = re.search(r"dcterms:modified[^>]*>([^<]{10})", core)
        if lm or md:
            flag += f"  [modified {md.group(1) if md else '?'} by {lm.group(1) if lm else '?'}]"
    except KeyError:
        pass
    return f"{len(lines)} paragraphs", txt, flag


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("directory")
    ap.add_argument("--out", default=None, help="where to write extracted text")
    a = ap.parse_args()
    out = a.out or os.path.join(os.environ.get("TEMP", "."), "ar_probe")
    os.makedirs(out, exist_ok=True)

    files = []
    for fn in sorted(os.listdir(a.directory)):
        p = os.path.join(a.directory, fn)
        if not os.path.isfile(p):
            continue
        ext = os.path.splitext(fn)[1].lower()
        if ext in (".pdf", ".xlsx", ".xlsm", ".docx", ".doc"):
            files.append((fn, p, ext))

    print(f"{'FILE':<58} {'SIZE':>9}  {'MODIFIED':<17} DETAIL")
    print("-" * 125)
    groups = {}
    for fn, p, ext in files:
        st = os.stat(p)
        mod = datetime.fromtimestamp(st.st_mtime).strftime("%Y-%m-%d %H:%M")
        detail, txt, flag = "", None, ""
        try:
            if ext == ".pdf":
                detail, txt, flag = do_pdf(p, out)
            elif ext in (".xlsx", ".xlsm"):
                detail, txt, flag = do_xlsx(p, out)
            elif ext == ".docx":
                detail, txt, flag = do_docx(p, out)
            else:
                detail = "legacy .doc, convert first"
        except Exception as e:
            detail = f"FAILED: {type(e).__name__}: {str(e)[:60]}"
        print(f"{fn[:58]:<58} {human(st.st_size):>9}  {mod:<17} {detail}{flag}")
        groups.setdefault(stem(fn) + ext, []).append((mod, fn))

    dupes = {k: v for k, v in groups.items() if len(v) > 1}
    if dupes:
        print("\nLIKELY VERSIONS OF THE SAME DOCUMENT  (newest first, read the newest)")
        for k, v in dupes.items():
            print(f"  {k}")
            for mod, fn in sorted(v, reverse=True):
                print(f"      {mod}   {fn}")

    print(f"\nExtracted text written to: {out}")
    print("\nBefore reading anything, state in the scope note which file and which")
    print("modification date you reviewed. Check that the Excel current year columns")
    print("are populated: empty current year against a full prior year means the")
    print("working set is last year's file, which is itself a finding under SA 230.")


if __name__ == "__main__":
    main()
