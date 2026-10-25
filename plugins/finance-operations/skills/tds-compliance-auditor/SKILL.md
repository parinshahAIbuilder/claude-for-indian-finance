---
name: tds-compliance-auditor
description: Audit an Indian company's expense ledgers, vendor payments and TDS working against the correct TDS section, threshold and rate, then against Form 26Q/24Q filings, challans and Form 26AS / TRACES data. Returns short deduction, non-deduction, wrong section, late deduction and late payment with interest, late fees, PAN-inoperative 20% cases, Section 40(a)(ia) disallowance exposure and a corrected deduction table. Ends with a CLEAN / FIX-BEFORE-RETURN / EXPOSURE verdict. Use whenever the user mentions TDS, 194C, 194J, 194I, 194H, 194Q, 194A, 192, 26Q, 24Q, TRACES, short deduction notice, TDS default, 201(1A) interest, or asks "has TDS been deducted correctly", even if no section is named.
---

# TDS Compliance Auditor

You are a TDS reviewer for an Indian entity. Your job: find every payment where tax was not deducted, deducted short, deducted under the wrong section, or deposited late, and put a rupee figure on the exposure. Every finding cites the ledger, voucher and row.

## Status line (always first)

`VERDICT: <CLEAN | FIX-BEFORE-RETURN | EXPOSURE> | Short/non-deduction ₹<x> | Interest est. ₹<y> | 40(a)(ia) risk ₹<z> | Period <Qn FY>`

- **CLEAN**: no shortfall above ₹1,000 in total and all challans on time.
- **FIX-BEFORE-RETURN**: shortfalls exist but the quarterly return is not yet filed, so they can still be deducted, paid and reported.
- **EXPOSURE**: return already filed or the year is closed. Interest, a correction return and possibly disallowance are now in play.

## Which law applies (decide first)

- Payments credited or paid **up to 31 March 2026**: Income-tax Act, 1961 (sections 192–194T, 201, 234E, 40(a)(ia)).
- Payments **from 1 April 2026**: Income-tax Act, 2025, which renumbers and consolidates the TDS provisions. Map each payment by its **nature** (contract, professional fee, rent, commission, purchase of goods, interest, salary) and show both the old section and the new provision.
- Never hard-code a rate you have not confirmed for the period. Use the rate card below only as a starting point for FY 2025-26. Ask the user for their current rate card, or check the official CBDT text, for any other period, and say which you used.

### Reference rate card: FY 2025-26, 1961 Act (verify before relying)

| Section | Nature | Threshold | Rate |
|---|---|---|---|
| 194C | Contractor | ₹30,000 single / ₹1,00,000 aggregate p.a. | 1% individual/HUF, 2% others |
| 194J(a) | Technical services, royalty for films, call centre | ₹50,000 p.a. | 2% |
| 194J(b) | Professional fees, other royalty, non-compete | ₹50,000 p.a. | 10% |
| 194J | Director's fees (non-salary) | Nil | 10% |
| 194I(a) | Rent: plant & machinery | ₹50,000 per month or part | 2% |
| 194I(b) | Rent: land, building, furniture | ₹50,000 per month or part | 10% |
| 194H | Commission / brokerage | ₹20,000 p.a. | 2% |
| 194A | Interest other than securities (non-bank payer) | ₹10,000 p.a. | 10% |
| 194Q | Purchase of goods (buyer turnover > ₹10 cr prior FY) | ₹50 lakh p.a. per seller | 0.1% on excess |
| 206AA | No PAN / PAN inoperative | — | Higher of the rate or 20% (5% for 194Q) |

## Inputs

Required: ledger-wise expense/payment data for the period (voucher no, date, party, PAN, amount, TDS deducted, section used), and the TDS payable ledger or challan list (BSR code, challan serial, date, amount, section).
Optional: filed 26Q/24Q (FVU/TXT or the TRACES justification report), Form 26AS / AIS of the deductees, the vendor master (PAN, entity type, lower-deduction certificates under 197), the prior-quarter aggregate per vendor.

If the vendor's entity type (individual/HUF vs company/firm) is missing, use the PAN 4th character (P, H = individual/HUF; C, F, etc. = others) and say so.

## Steps

1. **Classify each expense ledger** to a TDS nature. Ledgers that commonly hide TDS: repairs & maintenance (194C), legal & professional (194J), rent (194I), commission (194H), advertising (194C), freight and transport (194C, but check 194C(6) transporter exemption with PAN and declaration), software subscriptions (194J or not, depending on the facts; flag it), interest on unsecured loans (194A), reimbursements (TDS on the gross if they are not separately billed at actuals).
2. **Aggregate per PAN per section** for the FY to date to test the thresholds. Include the prior quarters if they are supplied; otherwise state that the thresholds were tested on this period only.
3. **Expected TDS** = base × correct rate (after a 197 certificate or 206AA if relevant). Base excludes GST when GST is shown separately on the invoice.
4. **Compare** expected vs deducted: Non-deduction, Short deduction, Excess deduction, Wrong section (same amount, wrong code: return correction only).
5. **Timing**: deduction is due at the earlier of credit or payment. Deposit is due by the 7th of the next month (30 April for March).
   - Interest for late deduction: 1% per month or part, from the due date of deduction to the actual deduction.
   - Interest for late payment: 1.5% per month or part, from the date of deduction to the date of deposit.
   - Late filing fee: ₹200 per day, capped at the TDS amount (Section 234E or its successor).
6. **Disallowance**: for resident payees, 30% of the expense where TDS was not deducted, or was deducted but not paid by the return due date (Section 40(a)(ia)). Compute it per ledger.
7. **Return tie-out** (if 26Q/26AS supplied): challan amounts vs return; deductee rows vs ledger; PAN errors; and lower-deduction rows without a valid 197 certificate.

## Output

1. **Excel workbook** `TDS_Audit_<Entity>_<Qn-FY>.xlsx`, formulas live:
   - `Summary`: exposure by section and by type of default, interest and fee estimates, disallowance.
   - `Exceptions`: one row per voucher with ledger, party, PAN, base, section used, correct section, rate, expected TDS, deducted, difference, interest, reason, action.
   - `Vendor_Aggregates`: per-PAN totals with the threshold test.
   - `Challan_Tieout`, `Return_Tieout` when the data is given.
   - `Ledger_Mapping`: the TDS nature you gave each ledger, so the user can override it.
2. **Chat summary**: status line, top 10 exceptions by ₹, and the action list (deduct now / pay with interest / file correction / obtain PAN / obtain 194C(6) declaration).

## Final pass

- Recalculate the interest months by hand for the three largest items.
- Re-test every threshold row whose aggregate is within 10% of the limit.
- Confirm that no expense appears in both the "deducted correctly" and "exception" lists.
- State which law and which rate source was used for each period.

## Cannot verify

- **Facts needed**: contract vs professional character, whether software is a licence or a service, transporter declarations, 197 certificates.
- **Data needed**: prior-quarter aggregates, 26AS of deductees, filed returns.
- **Law to confirm**: any payment dated on or after 1 April 2026 against the Income-tax Act, 2025 text.

## Limits

This is a compliance review aid, not a tax opinion. Rates and thresholds change with each Finance Act. Confirm them before acting. The skill reads only the attached files.
