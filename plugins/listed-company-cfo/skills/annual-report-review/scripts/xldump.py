#!/usr/bin/env python
"""Dump Excel working papers and run the working paper diagnostics.

    python xldump.py <book.xlsx>                        list sheets
    python xldump.py <book.xlsx> --sheet BS --rows 80   dump one sheet
    python xldump.py <book.xlsx> --all --out dump.txt   dump every visible sheet
    python xldump.py <book.xlsx> --diag                 formula errors, open notes, staleness
    python xldump.py <book.xlsx> --find "Total Current" search every sheet
    python xldump.py <book.xlsx> --roundtrip            does a library save damage this file?

Read values, not formulas, by default. Values are what printed.

--roundtrip answers the question you must settle before writing anything into a
client workbook. openpyxl reads these files correctly and destroys them on save:
a live 3 MB working set lost 86 relationship parts. Where it reports losses,
drive Excel through COM or deliver a separate workbook. See the review-markup
skill.
"""
import argparse, os, re, sys, zipfile

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

# Sheet name prefixes --all skips: trial balances, sub groupings and scratch
# tabs, which are long and are not what you are reviewing. Add the client's own
# prefixes here when a working set has its own convention.
SKIP = ("TB ", "TB", "Matrix", "trial_balance", "Sheet", "Sub Grouping",
        "pending", "SEBI")
ERRS = ("#REF!", "#VALUE!", "#DIV/0!", "#N/A", "#NAME?", "#NUM!")
NOTE = re.compile(r"to be (confirm|updated|discuss|check|received|shown)|pending|not done|"
                  r"to confirm|restate to confirm|not mentioned in report|bifurcation", re.I)


def fmt(v):
    if v is None:
        return ""
    if isinstance(v, float):
        return str(int(round(v))) if abs(v - round(v)) < 1e-9 and abs(v) < 1e15 else f"{v:.4f}".rstrip("0").rstrip(".")
    return str(v).replace("\n", " | ").strip()


def dump(ws, maxr, maxc):
    out, blank = [], 0
    for r in range(1, min(ws.max_row, maxr) + 1):
        vals = [fmt(ws.cell(r, c).value) for c in range(1, min(ws.max_column, maxc) + 1)]
        while vals and vals[-1] == "":
            vals.pop()
        if not vals:
            blank += 1
            if blank > 2:
                continue
            out.append(f"R{r}|")
            continue
        blank = 0
        out.append(f"R{r}| " + " | ".join(vals))
    return "\n".join(out)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("book")
    ap.add_argument("--sheet")
    ap.add_argument("--all", action="store_true")
    ap.add_argument("--diag", action="store_true")
    ap.add_argument("--find")
    ap.add_argument("--roundtrip", action="store_true")
    ap.add_argument("--formulas", action="store_true", help="show formulas instead of values")
    ap.add_argument("--rows", type=int, default=200)
    ap.add_argument("--cols", type=int, default=14)
    ap.add_argument("--out")
    a = ap.parse_args()

    if a.roundtrip:
        import openpyxl
        before = set(zipfile.ZipFile(a.book).namelist())
        tmp = os.path.join(os.environ.get("TEMP", "."), "_rt_test.xlsx")
        wb = openpyxl.load_workbook(a.book)
        wb.save(tmp)
        wb.close()
        after = set(zipfile.ZipFile(tmp).namelist())
        lost = sorted(before - after)
        os.remove(tmp)
        print(f"source parts   {len(before)}")
        print(f"after save     {len(after)}")
        print(f"PARTS LOST     {len(lost)}")
        if lost:
            print("\nDO NOT write into this workbook with openpyxl. Examples of what is lost:")
            for p in lost[:10]:
                print("   ", p)
            print("\nUse Excel COM, or deliver the additions as a separate workbook.")
        else:
            print("\nRound trip is clean. A library save is safe for this file.")
        return

    import openpyxl
    wb = openpyxl.load_workbook(a.book, data_only=not a.formulas)
    sheets = wb.sheetnames

    if a.find:
        pat = re.compile(a.find, re.I)
        for sn in sheets:
            ws = wb[sn]
            for r in range(1, min(ws.max_row, 500) + 1):
                for c in range(1, min(ws.max_column, a.cols) + 1):
                    v = ws.cell(r, c).value
                    if isinstance(v, str) and pat.search(v):
                        row = [fmt(ws.cell(r, x).value) for x in range(1, a.cols + 1)]
                        while row and row[-1] == "":
                            row.pop()
                        print(f"{sn}!R{r}C{c}  " + " | ".join(row)[:170])
        return

    if a.diag:
        print(f"{len(sheets)} sheets\n")
        for sn in sheets:
            ws = wb[sn]
            errs, notes, cur, pri = [], [], 0, 0
            for r in range(1, min(ws.max_row, 400) + 1):
                for c in range(1, min(ws.max_column, a.cols) + 1):
                    v = ws.cell(r, c).value
                    if v is None:
                        continue
                    s = str(v)
                    if s in ERRS:
                        errs.append(f"R{r}C{c}")
                    elif isinstance(v, str) and NOTE.search(s):
                        notes.append(f"R{r}: {s[:72]}")
                    elif isinstance(v, (int, float)):
                        if c == 3 or c == 4:
                            cur += 1
                        elif c == 5:
                            pri += 1
            flag = ""
            if pri > 6 and cur == 0:
                flag = "   CURRENT YEAR EMPTY, PRIOR YEAR POPULATED: this sheet is last year's"
            if errs or notes or flag:
                print(f"--- {sn}{flag}")
                if errs:
                    print(f"      formula errors ({len(errs)}): {', '.join(errs[:8])}")
                for n in notes[:4]:
                    print(f"      open note  {n}")
        return

    if a.all:
        buf = []
        for sn in sheets:
            if any(sn.startswith(k) for k in SKIP):
                continue
            buf.append(f"\n\n########## SHEET: {sn} ##########")
            buf.append(dump(wb[sn], a.rows, a.cols))
        text = "\n".join(buf)
        if a.out:
            open(a.out, "w", encoding="utf-8").write(text)
            print(f"wrote {len(text)} chars to {a.out}")
        else:
            print(text)
        return

    if a.sheet:
        sn = a.sheet if a.sheet in sheets else next((s for s in sheets if s.strip() == a.sheet.strip()), None)
        if not sn:
            print(f"no sheet {a.sheet!r}. Available:")
            for s in sheets:
                print("   ", repr(s))
            return
        print(f"########## {sn}  ({wb[sn].calculate_dimension()}) ##########")
        print(dump(wb[sn], a.rows, a.cols))
        return

    for s in sheets:
        ws = wb[s]
        print(f"  {s!r:48s} {ws.calculate_dimension():<16} {ws.sheet_state}")


if __name__ == "__main__":
    main()
