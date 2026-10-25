---
name: ncd-interest-register
description: Prepare the interest and redemption payout register for listed or unlisted Indian NCDs / debentures — holder-wise interest from the RTA benpos, day count per the trust deed, holiday convention, TDS under section 193 (with 197 certificates, 15G / 15H, 206AA, non-residents), net payout file, accounting entries and the related SEBI LODR intimations. Use whenever the user mentions NCD interest, debenture interest, coupon payment, benpos, record date, interest register, TDS on debenture interest, Reg 57, or redemption of NCDs, even if no section is named.
---

# NCD Interest Register

You are the treasury desk paying debenture holders. One wrong rupee to a holder becomes an investor complaint, a SCORES case and a trustee query. Every figure must trace to the benpos, the trust deed and the tax status of the holder.

## Ground rules

- **The trust deed and offer document decide the day count and payment terms.** Read them first. Common conventions: Actual/Actual (actual days over 365, or 366 when the period includes 29 February) as set out in SEBI's operational circulars for listed debt, and 30/360 (equal monthly or quarterly coupons) where the deed says so. If the deed and the SEBI convention differ, follow the deed for the amount and flag the difference to the CFO and the debenture trustee.
- **Holiday convention** for listed debt (per SEBI): if an interest date falls on a non-business day, pay on the next working day, with interest for the extra days included; the schedule of future dates does not shift. If a redemption date falls on a non-business day, pay on the previous working day, with interest up to that day. Confirm against the offer document.
- **Record date**: as fixed in the offer document (commonly 15 days before the payment date). Holders are taken from the benpos received from the RTA / depositories as of the record date.
- Never assume a holder's tax status. Use PAN status, residential status, and the certificates on file.

## Workflow

### 1. Inputs

ISIN, face value, number of NCDs outstanding, coupon rate, frequency, interest period start and end, payment date, day count clause, record date, benpos (holder name, PAN, DP / client ID, quantity, category, residential status, bank details), and tax documents (15G / 15H, section 197 certificates, tax residency certificates and Form 10F for non-residents). Flag anything missing.

### 2. Gross interest

Per holder: quantity × face value × coupon × day-count fraction. Show the fraction explicitly (for example 30/360 monthly = 1/12; Actual/Actual for a 92-day quarter = 92/365). Round per holder as the deed or RTA practice requires and state the rounding rule. Reconcile: sum of holders' quantities = NCDs outstanding.

### 3. TDS

| Holder type | Treatment (confirm the current Finance Act rates and thresholds) |
|---|---|
| Resident with valid PAN | Section 193 at the rate in force (10% at the time of writing), subject to any threshold available for the payer and holder type |
| Resident with 15G / 15H on file | No TDS, if the form is valid for the year and the holder is eligible |
| Section 197 lower / nil deduction certificate | Rate on the certificate, within its validity period and amount limit |
| PAN missing or inoperative | Section 206AA: higher of twice the normal rate or 20% |
| Mutual funds, insurers and other exempt entities | No TDS where the law exempts them; keep the supporting document |
| Non-resident | Section 195 at the treaty or Act rate, plus surcharge and cess where applicable; treaty rate only with TRC and Form 10F |

Since listed dematerialised debentures no longer enjoy a blanket TDS exemption for residents, do not skip TDS just because the NCDs are listed. Round TDS to the nearest rupee per holder.

### 4. Payout file and register

Columns: holder, PAN, DP / client ID, quantity, gross interest, TDS rate, TDS, net payable, bank account, IFSC, remarks (certificate reference, rate basis). Totals: gross, TDS, net, and a control check that gross − TDS = net.

### 5. Accounting entries

- Accrual (each month-end, even for quarterly coupons): Dr Finance cost / Cr Interest accrued but not due.
- Payment date: Dr Interest accrued / Cr Bank (net) and Cr TDS payable.
- TDS deposit by the 7th of the following month (30 April for March); quarterly Form 26Q; Form 16A to holders.
- Under Ind AS, finance cost is at the effective interest rate (including issue expenses amortised); the coupon register is the cash view. Show the difference if the user asks.

### 6. Regulatory intimations (listed NCDs)

- Reg 57(1): intimate the exchange and confirm payment status within one working day of the due date, using the format in SEBI's operational circular.
- Reg 57(4) and 57(5): quarterly statements of obligations falling due and certificate of payment status.
- Inform the debenture trustee; update the trustee's monitoring returns.
- Reg 50: prior intimation of record date where required.

## Output format

1. Workings sheet (day-count fraction, rate, rounding rule, deed clause reference).
2. Holder register with TDS and net payout.
3. Bank upload file (CSV in the bank's format if supplied).
4. Journal entries.
5. Draft Reg 57 intimation.
6. Open points (missing PANs, expired certificates, mismatched quantities).

## Failure modes to avoid

- Using Actual/365 when the deed says 30/360, or the reverse.
- Applying a section 197 certificate after its validity date or beyond its amount limit.
- Paying a holder who sold before the record date because an old benpos was used.
- Shifting all future interest dates after one holiday.
- Forgetting surcharge and cess on non-resident TDS.
