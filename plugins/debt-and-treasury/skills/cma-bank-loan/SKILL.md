---
name: cma-bank-loan
description: Prepare CMA (Credit Monitoring Arrangement) data for an Indian bank or NBFC loan proposal — Forms I to VI, MPBF / drawing power for working capital, term loan DSCR and repayment schedule, key ratios and a lender-ready note — from audited financials and a projection model. Use whenever the user mentions CMA data, CMA report, bank loan proposal, cash credit, overdraft, working capital limit, MPBF, drawing power, Tandon or Nayak committee, term loan appraisal, or asks "how much working capital can the bank give us", even if no form is named.
---

# CMA Data for Bank Loans

You prepare CMA data the way a credit analyst at an Indian bank will read it: consistent across all six forms, tied to audited numbers for past years, with projections that a sceptical appraiser cannot break in the first meeting.

## Ground rules

- Years: two audited years (minimum), current-year estimate, and projections for the loan tenor (usually 5–7 years for a term loan, 2 years for pure working capital).
- Every past-year figure must tie to the audited balance sheet and P&L. Show the tie-out.
- Presentation basis: banks appraise on an IGAAP-style view. For Ind AS reporters with heavy leases, reverse Ind AS 116 (rent back into expenses, ROU and lease liability out) and give a one-page reconciliation to the reported Ind AS numbers. Say which basis every table is on.
- Classify consistently: current liabilities exclude bank borrowings for working capital when computing MPBF; current maturities of long-term debt sit in current liabilities.
- Never plug. If the balance sheet does not balance, find the error.

## Workflow

### 1. Inputs

Ask for: audited financial statements, trial balance or ERP export for the current year, the projection model (or assumptions: revenue drivers, margins, capex, holding periods), existing and proposed facilities (lender, type, limit, rate, tenor, repayment, security), and promoter contribution. List what is missing.

### 2. Forms

| Form | Content | Checks |
|---|---|---|
| I | Particulars of existing and proposed limits | Ties to sanction letters |
| II | Operating statement (sales, cost of sales, operating profit, interest, PBT, tax, PAT) | Ties to audited P&L |
| III | Analysis of balance sheet (liabilities and assets, with current / non-current split) | Balances every year |
| IV | Comparative statement of current assets and current liabilities, with holding levels (raw material, WIP, finished goods in months of consumption or cost of sales; receivables in months of sales; creditors in months of purchases) | Holding levels reasonable vs history and industry |
| V | Computation of MPBF | See below |
| VI | Funds flow (long-term sources and uses, working capital changes) | Long-term sources should fund long-term uses |

### 3. Working capital assessment

- **Second method of lending (Tandon)**, the usual default for larger limits:
  Working capital gap (WCG) = total current assets − current liabilities other than bank borrowings.
  Minimum margin = 25% of total current assets.
  MPBF = WCG − 25% of current assets (equivalently, 75% of current assets − other current liabilities).
  Implied minimum current ratio = 1.33.
- **First method**: MPBF = 75% of WCG (margin 25% of the gap); current ratio can fall to about 1.17. Mention only if the lender uses it.
- **Turnover method (Nayak)** for smaller limits (historically up to ₹5 crore for MSMEs): working capital requirement = 25% of projected turnover; bank finance = 20% of turnover, promoter margin = 5%. Confirm the lender's current cap.
- **Cash budget method** for seasonal or service businesses where inventory is minimal.
- **Drawing power**: (eligible stock + receivables within the age limit) − margins as per sanction − creditors for goods. Prepare the stock statement format the lender will ask for monthly.

Service businesses (IT, co-working, consulting) carry little inventory; say so and steer towards a receivables-backed limit or a cash budget instead of forcing Form IV holding norms.

### 4. Term loan appraisal

- Repayment schedule with moratorium, structured to start once the asset produces cash.
- **DSCR** = (PAT + depreciation + interest on term loans + non-cash charges) ÷ (interest on term loans + principal repayment due in the year). Report each year, the average and the minimum. Typical lender comfort: average 1.5 or above, no year below about 1.2; confirm the lender's own floor.
- Fixed asset coverage ratio, promoter contribution %, debt-equity (TOL/TNW) and interest coverage.
- Break-even and sensitivity: revenue −10%, margin −2 points, rate +1%. Show DSCR under each.

### 5. Ratios page

Current ratio, TOL/TNW, debt-equity, DSCR, ISCR, PBT and PAT margins, inventory and receivable days, creditor days, return on capital employed. Comment on any ratio that moves more than 20% year on year.

### 6. Lender note

Two pages: the business, the purpose of the loan, the ask (facility, amount, tenor, security), past performance in three bullets, projections in three bullets, ratios table, risks and mitigants, and the Ind AS to IGAAP bridge if relevant. Board-appropriate language, figures in ₹ crore.

## Output format

1. Excel workbook: Inputs, Forms I–VI, MPBF, Term loan schedule, DSCR, Ratios, Sensitivity, Reconciliation (to audited and to Ind AS). Formulas, not hardcoded results.
2. Lender note (Word or PDF on request).
3. Open points list for the CFO.

## Failure modes to avoid

- Projected current ratio below 1.33 while asking for full MPBF under the second method.
- Holding levels that improve dramatically in year one with no operational reason.
- Ignoring current maturities of long-term debt in Form III.
- Mixing Ind AS EBITDA (rent excluded) with IGAAP peers when the banker benchmarks the sector.
- DSCR that only works because the moratorium hides the first repayment years.
