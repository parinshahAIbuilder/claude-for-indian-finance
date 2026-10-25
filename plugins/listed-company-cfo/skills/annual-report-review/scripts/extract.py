#!/usr/bin/env python
"""Layout preserving text from a PDF page range, or text from a docx.

    python extract.py <file.pdf> <from> <to>
    python extract.py <file.pdf> <from> <to> --render OUT --dpi 200
    python extract.py <file.docx>

Pages are 1 based pdf pages. Work in ranges of at most twenty five pages.

Do not use `pdftotext -layout`: on a tight financial table it approximates
columns with spaces, the approximation collapses, and figures land under the
wrong heading silently.

Use --render for pages that are scans or vector outlines, and whenever you are
deciding whether a digit is an 8 or a 0. Then read the PNGs.
"""
import argparse, os, sys, zipfile
from xml.etree import ElementTree as ET

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
W = "{http://schemas.openxmlformats.org/wordprocessingml/2006/main}"


def docx_text(path):
    z = zipfile.ZipFile(path)
    root = ET.fromstring(z.read("word/document.xml"))
    body = root.find(W + "body")
    out = []
    for ch in body:
        tag = ch.tag.split("}")[1]
        if tag == "p":
            out.append("".join(n.text or "" for n in ch.iter(W + "t")).strip())
        elif tag == "tbl":
            out.append("  <<TABLE>>")
            for tr in ch.findall(W + "tr"):
                cells = ["".join(n.text or "" for n in tc.iter(W + "t")).strip().replace("\n", " ")
                         for tc in tr.findall(W + "tc")]
                out.append("  | " + " | ".join(cells))
            out.append("  <<END TABLE>>")
    res, blank = [], 0
    for ln in out:
        if not ln:
            blank += 1
            if blank > 1:
                continue
        else:
            blank = 0
        res.append(ln)
    return "\n".join(res)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("file")
    ap.add_argument("start", nargs="?", type=int)
    ap.add_argument("end", nargs="?", type=int)
    ap.add_argument("--render", help="write page PNGs to this directory instead of text")
    ap.add_argument("--dpi", type=int, default=170)
    a = ap.parse_args()

    if a.file.lower().endswith((".docx", ".dotx")):
        print(docx_text(a.file))
        return

    if a.render:
        import pymupdf
        os.makedirs(a.render, exist_ok=True)
        d = pymupdf.open(a.file)
        lo = (a.start or 1) - 1
        hi = min(a.end or a.start or len(d), len(d))
        for i in range(lo, hi):
            p = os.path.join(a.render, f"p{i+1:03d}.png")
            d[i].get_pixmap(dpi=a.dpi).save(p)
            print("wrote", p)
        d.close()
        return

    import pdfplumber
    with pdfplumber.open(a.file) as pdf:
        lo = (a.start or 1) - 1
        hi = min(a.end or a.start or len(pdf.pages), len(pdf.pages))
        for i in range(lo, hi):
            print(f"\n\n########## PAGE {i+1} ##########")
            print(pdf.pages[i].extract_text(layout=True) or "")


if __name__ == "__main__":
    main()
