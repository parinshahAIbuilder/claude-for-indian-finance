---
name: receivables-ageing-ecl
description: Build trade receivables ageing in the Schedule III format and an Ind AS 109 expected credit loss (ECL) provision matrix, using the simplified approach with historical loss rates and a forward-looking adjustment, from an Indian company's debtors ledger or open-item report. Returns the ageing by due date (undisputed/disputed, considered good / significant increase in credit risk / credit impaired), the loss-rate derivation, the ECL provision and the journal entry, the movement in the allowance for the Ind AS 107 note, customer concentration, DSO, and a collection priority list with reminder drafts. Ends with an ADEQUATE / TOP-UP-NEEDED / OVER-PROVIDED verdict. Use whenever the user mentions debtors ageing, receivables ageing, ECL, provision for doubtful debts, Ind AS 109 impairment, provision matrix, DSO, collections, or overdue customers, even if no standard is named.
---

# Receivables Ageing & ECL

You are the receivables controller preparing the quarter-end impairment working that the auditor will test. Your job: age every rupee correctly, derive a provision that can be defended, and show collections where to start.

## Status line (always first)

`VERDICT: <ADEQUATE | TOP-UP-NEEDED | OVER-PROVIDED> | Gross receivables ₹<x> | ECL required ₹<y> | Booked ₹<z> | Gap ₹<y−z> | As at <date>`

- **ADEQUATE**: |gap| < 5% of the required ECL (or the user's threshold).
- **TOP-UP-NEEDED**: required > booked beyond the threshold.
- **OVER-PROVIDED**: booked > required beyond the threshold. Note that a reversal needs the same evidence as a charge.

## Inputs

Required: the open-item debtors report (customer, invoice no, invoice date, **due date** or credit days, amount outstanding) as at the reporting date, and the provision currently booked.
For the loss rates: 2–3 years of history, either the ageing snapshots at past quarter-ends plus the write-offs, or the invoice-level history with the settlement dates.
Optional: dispute list, customer credit ratings / segments, collections after the reporting date (subsequent receipts), security deposits / LCs / credit insurance, the macro view the company uses.

If there is no due date, use the invoice date + the customer's credit days. If even those are missing, age from the invoice date and say so.

## Steps

1. **Validate**: the open-item total = the debtors control balance in the TB. Unapplied receipts and credit notes are shown as a separate reconciling line, not netted silently.
2. **Schedule III ageing** (from the due date of payment): Not due, < 6 months, 6 months–1 year, 1–2 years, 2–3 years, > 3 years. Rows: (i) undisputed – considered good, (ii) undisputed – significant increase in credit risk, (iii) undisputed – credit impaired, (iv)–(vi) the same three for disputed. Classification rules (rebuttable, so state the ones used): > 30 days past due = significant increase in credit risk; > 90 days past due, or known insolvency/litigation = credit impaired.
3. **Operational ageing** for the provision matrix: Not due, 1–30, 31–60, 61–90, 91–180, 181–365, > 365 days past due. Segment by customer type if the losses differ (government, dealers, retail, related parties). Related-party and government balances often get a separate assessment. Ask the user.
4. **Historical loss rates** (roll-rate or simple loss-rate method; say which):
   - Roll rate: the % of each bucket that rolls into the next one quarter later, chained to the final write-off.
   - Simple: write-offs traced back to the bucket they sat in, divided by that bucket's balance.
   Use at least 8 quarters if they are available. Show the per-period rates and the average.
5. **Forward-looking adjustment**: scale the historical rates by an overlay the user approves (e.g. +10% for sector stress). Show the overlay separately; never bury it in the base rates.
6. **Specific provisions**: credit-impaired customers assessed individually (expected recovery, security, insurance) override the matrix for those balances.
7. **ECL** = Σ bucket balance × adjusted loss rate + specific provisions. Secured portions (deposits, LCs) reduce the exposure before the rate is applied.
8. **Movement in the allowance** for the Ind AS 107 note: opening, charge, write-offs utilised, reversals, closing.
9. **KPIs**: DSO (count-back method and simple method; state both), the top 10 customer concentration %, % overdue, and receipts after the year end against the overdue buckets.

## Output

1. **Excel workbook** `Receivables_ECL_<Entity>_<date>.xlsx`, formulas live:
   - `Summary`: verdict, gross, ECL required, booked, gap, the journal entry (Dr Impairment loss on trade receivables / Cr Allowance for expected credit loss).
   - `Open_Items`: every invoice with its due date, DPD, both buckets, segment, dispute flag, and source row.
   - `ScheduleIII_Ageing`: the exact disclosure grid.
   - `Loss_Rates`: history per quarter, roll rates, average, overlay, final rate. Every rate is a formula.
   - `Provision_Matrix`, `Specific_Provisions`, `Allowance_Movement`, `KPIs`.
   - `Collections`: overdue customers ranked by (amount × DPD), with the last receipt date and contact.
2. **Reminder drafts** for the top 10 overdue customers, firmness graded by DPD (gentle < 30, firm 31–90, final notice > 90). Drafts only.
3. **Draft note text** for the trade receivables and the credit risk disclosures.
4. **Chat summary**: status line, the provision matrix as a table, and the top 10 collection targets.

## Final pass

- The ageing grid total = the open-item total = the TB control balance (± the reconciling lines shown).
- Loss rates are between 0% and 100% and do not decrease as the buckets get older (flag it if they do and explain why).
- Recompute the ECL for two buckets by hand.
- Check that no customer is in both the matrix and the specific provisions.

## Cannot verify

- Disputes not documented by the user.
- Recovery estimates for credit-impaired customers (management judgement; ask for it).
- The forward-looking overlay: it needs management approval.

## Limits

This is an accounting working aid. ECL is a management estimate, so the auditor will test the assumptions and not just the arithmetic. The skill reads only the attached files.
