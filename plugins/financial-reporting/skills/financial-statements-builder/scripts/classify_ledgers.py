#!/usr/bin/env python3
"""
classify_ledgers.py — first-pass FSLI mapping of a canonical trial balance.

Input : CSV/XLSX in canonical schema (see references/01-data-ingestion.md). Required columns:
        ledger_name, closing_balance. Optional: ledger_code, erp_group, erp_account_type, entity.
        Sign convention: debit positive, credit negative.
Output: mapping CSV with fsli, note_no, cash_flow_bucket, rule_used, confidence, rationale,
        plus flags for sign anomalies, suspense ledgers and likely duplicates.

The output is a PROPOSAL for review. Low-confidence rows must go to Open Points.

Usage: python classify_ledgers.py tb.csv mapping_out.csv [--framework indas|as|ifrs|usgaap]
"""
import argparse
import csv
import difflib
import re
import sys

import pandas as pd

# (fsli, note_no, cash_flow_bucket, nature) ; nature: A asset, L liability, E equity, I income, X expense
RULES = [
    (r"suspense|unclassified|clearing|difference in opening|temp(orary)? a/?c", ("SUSPENSE - RESOLVE", "", "", "?")),
    (r"interest income|interest on fd|interest on deposit|dividend income|profit on sale|gain on|foreign exchange gain|misc(ellaneous)? income|other income|discount received", ("Other income", "21", "PL", "I")),
    (r"interest on|interest expense|finance cost|processing fee|loan charges|bank interest", ("Finance costs", "26", "PL", "X")),
    (r"term loan|\bncd\b|debenture|overdraft|\bod\b|cash credit|\bcc a/?c|working capital|\becb\b|vehicle loan|borrowing|loan from|unsecured loan|secured loan", ("Borrowings", "14", "Financing", "L")),
    (r"accumulated depreciation|acc\.? dep|provision for depreciation", ("Property, plant and equipment (acc. dep.)", "3", "Investing", "A")),
    (r"capital work.?in.?progress|\bcwip\b", ("Capital work-in-progress", "3", "Investing", "A")),
    (r"right.?of.?use|\brou\b", ("Right-of-use assets", "3", "Investing", "A")),
    (r"lease liabilit", ("Lease liabilities", "15", "Financing", "L")),
    (r"goodwill", ("Goodwill", "4", "Investing", "A")),
    (r"software|licen[cs]e|trademark|patent|intangible", ("Other intangible assets", "4", "Investing", "A")),
    (r"building|plant|machinery|furniture|fixture|computer|vehicle|office equipment|leasehold improvement|fit.?out|air condition", ("Property, plant and equipment", "3", "Investing", "A")),
    (r"capital advance", ("Other non-current assets", "11", "Investing", "A")),
    (r"mutual fund|\bmf\b|investment in|shares of|bonds?\b|debenture.*(investment)", ("Investments", "5", "Investing", "A")),
    (r"deferred tax", ("Deferred tax (net)", "7", "Operating-NonCash", "A")),
    (r"stock|inventor|raw material|finished goods|work.?in.?process", ("Inventories", "8", "Operating-WC", "A")),
    (r"cash in hand|cash on hand|petty cash|^cash$", ("Cash and cash equivalents", "10", "Cash", "A")),
    (r"fixed deposit|\bfd\b|term deposit|margin money|earmarked|unpaid dividend a/?c", ("Other bank balances", "10", "Investing", "A")),
    (r"bank|hdfc|icici|sbi|axis|kotak|yes bank|idfc|indusind|federal|rbl|\bcurrent a/?c", ("Cash and cash equivalents", "10", "Cash", "A")),
    (r"security deposit.*(paid|given)|deposit.*(rent|landlord|electricity)|rent deposit", ("Other financial assets", "6", "Operating-WC", "A")),
    (r"security deposit.*(received|from)|deposit.*(client|customer|member)", ("Other financial liabilities", "17", "Operating-WC", "L")),
    (r"interest accrued.*(receiv|on fd|on deposit)", ("Other financial assets", "6", "Investing", "A")),
    (r"interest accrued", ("Other financial liabilities", "17", "Financing", "L")),
    (r"staff advance|employee advance|loan to|advance to employee", ("Loans", "6", "Operating-WC", "A")),
    (r"prepaid|input|itc|cgst.*input|sgst.*input|igst.*input|gst receivable|vat receivable|balance with (gst|government|statutory)", ("Other current assets", "11", "Operating-WC", "A")),
    (r"advance (tax|income tax)|tds receivable|tcs receivable|income tax refund", ("Current tax assets (net)", "11", "Tax", "A")),
    (r"provision for (income )?tax|income tax payable", ("Current tax liabilities (net)", "19", "Tax", "L")),
    (r"advance (to|paid to) (supplier|vendor)", ("Other current assets", "11", "Operating-WC", "A")),
    (r"unbilled", ("Other financial assets", "6", "Operating-WC", "A")),
    (r"debtor|receivable|customer", ("Trade receivables", "9", "Operating-WC", "A")),
    (r"share capital|equity shares", ("Equity share capital", "12", "Financing", "E")),
    (r"securities premium|share premium|general reserve|retained earning|surplus|profit and loss a/?c|capital reserve|oci reserve|esop reserve|share option", ("Other equity", "13", "Equity", "E")),
    (r"msme|micro.*small", ("Trade payables - MSME", "16", "Operating-WC", "L")),
    (r"creditor|payable for expense|trade payable|vendor|supplier", ("Trade payables - others", "16", "Operating-WC", "L")),
    (r"capital creditor", ("Other financial liabilities", "17", "Investing", "L")),
    (r"salary payable|wages payable|bonus payable|employee dues|reimbursement payable", ("Other financial liabilities", "17", "Operating-WC", "L")),
    (r"gratuity|leave encash|compensated absence|provision for", ("Provisions", "18", "Operating-WC", "L")),
    (r"tds payable|gst payable|output|cgst|sgst|igst|\bpf payable|esi payable|professional tax|statutory dues|tcs payable", ("Other current liabilities", "19", "Operating-WC", "L")),
    (r"advance from customer|customer advance|deferred revenue|income received in advance|contract liabilit", ("Other current liabilities", "19", "Operating-WC", "L")),
    (r"sales|revenue|service income|rental income|licen[cs]e fee income|seat|subscription income|income from operations", ("Revenue from operations", "20", "PL", "I")),
    (r"purchase", ("Purchases of stock-in-trade / materials", "22", "PL", "X")),
    (r"salar|wages|bonus|contribution to (pf|provident|esi)|staff welfare|gratuity expense|esop expense|employee benefit|incentive", ("Employee benefits expense", "25", "PL", "X")),
    (r"depreciation|amortisation|amortization", ("Depreciation and amortisation expense", "27", "Operating-NonCash", "X")),
    (r"current tax|income tax expense|tax expense|mat credit", ("Tax expense", "29", "Tax", "X")),
    (r"rent|power|electricity|repair|maintenance|legal|professional|audit fee|insurance|travel|conveyance|printing|stationery|telephone|internet|advertis|marketing|commission|brokerage|csr|donation|bank charges|rates and taxes|housekeeping|security charges|communication|loss on|bad debt|provision for doubtful|foreign exchange loss|miscellaneous expense|office expense|software expense|subscription expense", ("Other expenses", "28", "PL", "X")),
]
COMPILED = [(re.compile(p, re.I), v) for p, v in RULES]

ERP_TYPE_HINT = {
    "asset": "A", "fixed asset": "A", "bank": "A", "cash": "A", "accounts receivable": "A",
    "other current asset": "A", "stock": "A",
    "liability": "L", "accounts payable": "L", "other current liability": "L",
    "long term liability": "L", "credit card": "L",
    "equity": "E", "income": "I", "other income": "I", "expense": "X", "other expense": "X",
    "cost of goods sold": "X",
}


def classify_row(name: str, erp_type: str, bal: float):
    nature_hint = ERP_TYPE_HINT.get((erp_type or "").strip().lower())
    for rx, (fsli, note, cfb, nature) in COMPILED:
        if rx.search(name or ""):
            if nature == "?":
                return fsli, note, cfb, "suspense keyword", "Low", "Suspense/clearing ledger — must be resolved, never mapped to Other"
            if nature_hint and nature_hint != nature:
                return fsli, note, cfb, "name keyword (conflicts with ERP type)", "Low", f"Name suggests {nature}, ERP type suggests {nature_hint}"
            conf = "High" if nature_hint == nature else "Medium"
            return fsli, note, cfb, "name keyword" + (" + ERP type" if nature_hint else ""), conf, f"Matched pattern '{rx.pattern[:40]}'"
    if nature_hint:
        default = {"A": ("Other current assets", "11", "Operating-WC"), "L": ("Other current liabilities", "19", "Operating-WC"),
                   "E": ("Other equity", "13", "Equity"), "I": ("Other income", "21", "PL"), "X": ("Other expenses", "28", "PL")}[nature_hint]
        return (*default, "ERP type only", "Low", "No name match; defaulted by ERP account type")
    guess = ("Other current assets", "11", "Operating-WC") if bal > 0 else ("Other current liabilities", "19", "Operating-WC")
    return (*guess, "sign only", "Low", "No name or ERP-type signal; classified by balance sign — review")


def sign_flag(fsli: str, bal: float) -> str:
    if fsli.startswith("Trade payables") and bal > 0:
        return "Debit-balance creditor: reclassify to advances to suppliers"
    if fsli == "Trade receivables" and bal < 0:
        return "Credit-balance debtor: reclassify to advance from customers"
    if fsli == "Cash and cash equivalents" and bal < 0:
        return "Credit bank balance: reclassify to borrowings (OD/CC)"
    if fsli == "Property, plant and equipment" and bal < 0:
        return "Negative gross block: investigate"
    return ""


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("tb")
    ap.add_argument("out")
    ap.add_argument("--framework", default="indas")
    a = ap.parse_args()

    df = pd.read_excel(a.tb) if a.tb.lower().endswith((".xlsx", ".xls")) else pd.read_csv(a.tb)
    df.columns = [c.strip().lower() for c in df.columns]
    for col in ("ledger_name", "closing_balance"):
        if col not in df.columns:
            sys.exit(f"Missing required column: {col}")
    df["closing_balance"] = pd.to_numeric(df["closing_balance"].astype(str).str.replace(",", ""), errors="coerce").fillna(0)
    erp = df["erp_account_type"] if "erp_account_type" in df.columns else pd.Series([""] * len(df))

    rows = []
    for i, r in df.iterrows():
        fsli, note, cfb, rule, conf, why = classify_row(str(r["ledger_name"]), str(erp.iloc[i]), r["closing_balance"])
        rows.append({
            "entity": r.get("entity", ""), "ledger_code": r.get("ledger_code", ""), "ledger_name": r["ledger_name"],
            "closing_balance": r["closing_balance"], "fsli": fsli, "note_no": note, "cash_flow_bucket": cfb,
            "rule_used": rule, "confidence": conf, "rationale": why, "sign_flag": sign_flag(fsli, r["closing_balance"]),
            "duplicate_suspect": "", "reviewer_override": "",
        })

    names = [str(x["ledger_name"]).lower() for x in rows]
    for i in range(len(names)):
        for j in range(i + 1, len(names)):
            if difflib.SequenceMatcher(None, names[i], names[j]).ratio() >= 0.85:
                rows[i]["duplicate_suspect"] = (rows[i]["duplicate_suspect"] + f"; {rows[j]['ledger_name']}").strip("; ")
                rows[j]["duplicate_suspect"] = (rows[j]["duplicate_suspect"] + f"; {rows[i]['ledger_name']}").strip("; ")

    with open(a.out, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        w.writeheader()
        w.writerows(rows)

    tb_total = round(df["closing_balance"].sum(), 2)
    low = sum(1 for x in rows if x["confidence"] == "Low")
    susp = [x for x in rows if x["fsli"].startswith("SUSPENSE") and abs(x["closing_balance"]) > 0.005]
    print(f"Ledgers: {len(rows)} | TB sum (should be 0): {tb_total} | High: {sum(x['confidence']=='High' for x in rows)} "
          f"| Medium: {sum(x['confidence']=='Medium' for x in rows)} | Low: {low}")
    print(f"Sign anomalies: {sum(1 for x in rows if x['sign_flag'])} | Duplicate suspects: {sum(1 for x in rows if x['duplicate_suspect'])} "
          f"| Suspense with balance: {len(susp)}")
    if abs(tb_total) > 1:
        print("CRITICAL: trial balance does not balance — stop and report.")
        sys.exit(2)


if __name__ == "__main__":
    main()
