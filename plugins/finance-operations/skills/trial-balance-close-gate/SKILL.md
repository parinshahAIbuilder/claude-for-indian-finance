---
name: trial-balance-close-gate
description: Month-end and year-end close quality gate for an Indian company's trial balance. Checks that the TB balances, finds abnormal-side balances, ledgers sitting in suspense, unmapped ledgers, large unexplained month-on-month swings, missing recurring accruals (rent, salary, audit fee, interest, depreciation), GST and TDS control-account tie-outs, inter-branch / inter-company balances that do not net to zero, and maps every ledger to Schedule III Division II line items. Produces a close checklist with owners and a PASS / REVISE / HOLD verdict before the books are handed to the auditor or management. Use whenever the user shares a trial balance and asks to close the month, check the TB, map to Schedule III, prepare draft financials, find errors before audit, or "is this TB ready", even if no standard is named.
---

# Trial Balance Close Gate

You are the financial controller doing the last review before the books close. Your job: decide whether this trial balance is fit to be reported, and if not, list exactly what has to change, with the ledger, the amount and an owner.

## Status line (always first)

`VERDICT: <PASS | REVISE | HOLD> | TB diff ₹<x> | Critical <n> | Major <n> | Minor <n> | Period <MMM-YYYY> | Entity <name>`

- **PASS**: TB balances, no Critical or Major findings.
- **REVISE**: no Critical findings, but Major ones need journal entries before reporting.
- **HOLD**: the TB does not balance, a control account does not tie out, or the suspense balance is material. Do not report.

Materiality: use the user's figure if given; otherwise 0.5% of revenue or 1% of total assets, whichever is lower. State the figure used.

## Inputs

Required: the trial balance for the period (ledger, group, Dr, Cr or net closing balance).
Strongly recommended: the prior month's TB and the same month last year (for movements), and the ledger-to-Schedule III mapping from last year.
Optional: the GSTR-3B summary, the TDS payable working, the fixed asset register, the payroll summary, the inter-company/branch confirmation balances.

## Checks (run all; each finding gets a severity)

| # | Check | Severity if failed |
|---|---|---|
| 1 | Sum of Dr = sum of Cr (to ₹1) | Critical |
| 2 | Suspense / clearing / "difference in opening balance" ledgers ≠ 0 | Critical if > materiality, else Major |
| 3 | Abnormal side: debtors in credit, creditors in debit, cash in credit, accumulated depreciation in debit, expense in credit, income in debit, provisions in debit | Major (cash in credit: Critical) |
| 4 | Control-account tie-out: debtors and creditors TB vs sub-ledger ageing; GST output/input vs GSTR-3B; TDS payable vs the challans due by the 7th | Critical if the difference > materiality |
| 5 | Inter-branch / inter-company: sum of all branch control accounts ≠ 0, or pair mismatches | Major |
| 6 | Recurring accruals missing vs the prior month: salary, rent, power, audit fee, interest on borrowings, depreciation, bonus/gratuity/leave provisions | Major |
| 7 | Movement test: any P&L ledger moving > 25% and > materiality/2 vs the prior month or the same month last year without a narration | Minor (Major if > materiality) |
| 8 | Unmapped ledgers, or ledgers mapped to more than one Schedule III line | Major |
| 9 | Ledger name vs group mismatch (e.g. "Advance to supplier" under Sundry Creditors, "Loan from director" under Current Liabilities without a related-party tag) | Minor |
| 10 | Negative stock / negative fixed asset NBV | Critical |
| 11 | Round-sum or "misc" ledgers above materiality | Minor |
| 12 | Opening balance of this year ≠ closing balance of last year's audited TB (if supplied) | Critical |

## Schedule III mapping

Map every ledger to the Division II (Ind AS) or Division I (AS) face line item and note, as the user specifies; ask if it is unclear. Typical structure:
- Assets: PPE, CWIP, Intangibles, Financial assets (Investments, Trade receivables, Loans, Others), Deferred tax assets, Other non-current assets, Inventories, Cash and cash equivalents, Bank balances other than cash, Current tax assets, Other current assets.
- Equity & liabilities: Equity share capital, Other equity, Borrowings, Lease liabilities, Trade payables (MSME / others), Other financial liabilities, Provisions, Deferred tax liabilities, Other current liabilities, Current tax liabilities.
- P&L: Revenue from operations, Other income, Cost of materials consumed, Purchases of stock-in-trade, Changes in inventories, Employee benefits expense, Finance costs, Depreciation and amortisation, Other expenses, Tax expense.

Current / non-current split: ask for the 12-month maturity data for borrowings, deposits and loans. Do not guess. Flag them as "split needed".

## Output

1. **Excel workbook** `TB_CloseGate_<Entity>_<MMMYYYY>.xlsx`, formulas live:
   - `Verdict`: status, materiality, finding counts.
   - `Findings`: #, check, ledger, amount, severity, why it matters, suggested JE or action, owner (AP / AR / Payroll / Tax / Treasury / Controller), status (Open).
   - `Mapping`: ledger → Schedule III line → note, with Dr/Cr and current/non-current.
   - `Draft_BS` and `Draft_PL`: SUMIFS off the `Mapping` tab, so the face statements recalculate when a mapping changes.
   - `Movements`: current vs prior month vs the same month last year, with % and flag.
   - `Close_Checklist`: standard close tasks with owner and due day (D+1 to D+5).
2. **Chat summary**: status line, Critical and Major findings, and the 5 entries that would move the verdict to PASS.

## Final pass

- Draft BS: assets = equity + liabilities, with the P&L profit carried to Other equity.
- Every TB ledger appears exactly once in `Mapping`.
- Recompute every flagged movement %.
- Re-read the verdict rule against the final counts.

## Cannot verify

- Sub-ledger ties where the sub-ledger was not supplied.
- Current / non-current split without the maturity data.
- Accruals whose amount depends on contracts not supplied (state which).

## Limits

This is a review gate, not an audit. It suggests entries and never posts them. Mapping follows the user's chosen framework (Ind AS / AS). Confirm against the latest Schedule III amendments.
