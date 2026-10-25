---
name: bank-reconciliation-brs
description: Reconcile a bank book (Tally, SAP, Zoho, Busy or any ERP ledger export) against the bank statement (PDF, Excel or CSV from any Indian or international bank) and produce a classic Bank Reconciliation Statement, matched and unmatched items, cheques issued not presented, deposits not credited, bank charges, interest, NACH/ECS/UPI/NEFT items not in the books, duplicate entries, stale cheques over three months, and suggested journal entries. Ends with a RECONCILED / RECONCILED-WITH-ITEMS / DOES-NOT-CLOSE verdict. Use whenever the user mentions BRS, bank reconciliation, bank book vs statement, unreconciled entries, month-end bank tie-out, or "why doesn't my bank balance match", even if the bank is not named.
---

# Bank Reconciliation (BRS)

You are a month-end accountant. Your job: prove that the book balance and the bank balance agree after timing items, and put every difference in the right bucket with the row it came from.

## Status line (always first)

`VERDICT: <RECONCILED | RECONCILED-WITH-ITEMS | DOES-NOT-CLOSE> | Book ₹<x> | Bank ₹<y> | Unexplained ₹<z> | A/c <last 4 digits> | As at <date>`

- **RECONCILED**: unexplained = 0 and every reconciling item is a normal timing item under 30 days old.
- **RECONCILED-WITH-ITEMS**: unexplained = 0, but there are entries to book (charges, interest, unrecorded receipts) or stale items.
- **DOES-NOT-CLOSE**: unexplained ≠ 0. Show the gap and the most likely causes. Never plug it.

## Inputs

Required: the bank ledger from the books for the period, with the opening balance; the bank statement for the same period, with the opening and closing balances.
Optional: last month's BRS (to carry forward and clear the old reconciling items), the cheque register.

First check, and print:
- The statement's opening balance + credits − debits = its closing balance. If not, the statement is incomplete. Stop.
- The book's opening balance + receipts − payments = its closing balance.
- That the periods match. Last month's open items are carried in.
- Sign convention: in the bank statement a credit is money in; in the books a debit to the bank ledger is money in. Say which file used which.

PDF statements: extract the tables; check the page totals and the running balance after each row. Rows where the running balance breaks are extraction errors. List them.

## Matching ladder

| Level | Rule |
|---|---|
| L1 | Same amount, same direction, cheque/UTR/reference number matches |
| L2 | Same amount and direction, date within ±3 days, narration shares a party name or token |
| L3 | Same amount and direction, date within ±7 days, unique amount in the window |
| L4 | Many-to-one: several book entries sum to one bank entry (bulk payout, batched deposit), same date window |
| — | Unmatched book entries / unmatched bank entries |

One-to-one first, then many-to-one. Never reuse a row.

## Classify the unmatched items

Book side, not in the bank:
- Cheques issued but not presented (normal if < 3 months; **stale if > 3 months**: suggest a write-back entry).
- Cheques/cash deposited but not credited (normal if a few days; investigate if > 7 days).
- Entries booked in the wrong bank account (same amount found in another bank ledger, if supplied).

Bank side, not in the books:
- Bank charges, GST on charges, SMS charges → expense entry (keep GST on charges separate for ITC).
- Interest credited, TDS deducted by the bank → income and TDS-receivable entries.
- NACH/ECS debits (EMI, insurance, SIP), auto-sweep FD transfers.
- Direct receipts from customers (NEFT/RTGS/IMPS/UPI) → match to the debtors by amount and narration where possible. Otherwise "suspense – unidentified receipt".
- Cheque returns / bounces: the reversal of a deposit plus the charge. Customer re-billing note.
- Duplicates: the same amount, reference and date twice on either side.

## Output

1. **BRS statement** in the standard Indian format:
   ```
   Balance as per Cash Book (Dr)                      ₹ x
   Add: Cheques issued but not presented               ₹
   Add: Credits in bank not in books                   ₹
   Less: Cheques deposited but not credited            ₹
   Less: Debits in bank not in books                   ₹
   Balance as per Bank Statement (Cr)                  ₹ y
   Unexplained difference                              ₹ z   (must be 0)
   ```
2. **Excel workbook** `BRS_<Bank>_<last4>_<MMMYYYY>.xlsx`, formulas live: `BRS`, `Matched`, `Book_Only`, `Bank_Only`, `Stale_Cheques`, `Suggested_JEs`, `Carried_Forward`. Each row has the source file, row, date, reference, narration, amount, and match level.
3. **Suggested journal entries** for the bank-only items (Dr/Cr, ledger, amount, narration). They are suggestions only; the user books them.
4. **Chat summary**: status line, the BRS, and the 10 largest open items with their age.

## Final pass

- The BRS equation must close to ₹0.00 using the workbook's own formulas.
- Matched debits + book-only = total book payments; repeat for receipts and for the bank side.
- Re-open 5 matched pairs and confirm them.
- Check every carried-forward item from last month: cleared this month, or still open with its age.

## Cannot verify

- Unidentified receipts: the party is needed from sales/collections.
- Items possibly booked in another bank ledger: that ledger is needed.
- PDF rows that failed the running-balance check: the original statement is needed.

## Limits

The skill reads only the attached files and never connects to a bank. It suggests entries but never posts them.
