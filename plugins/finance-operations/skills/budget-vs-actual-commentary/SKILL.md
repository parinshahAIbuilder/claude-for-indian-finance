---
name: budget-vs-actual-commentary
description: Turn a budget file and an actuals file (GL, trial balance or MIS, single entity or branch-wise / cost-centre-wise / region-wise) into a Budget vs Actual pack, with month and year-to-date variances, favourable/adverse flags that respect the sign of revenue vs cost, price/volume/mix splits where units are given, a full-year re-forecast, and management commentary that explains each material variance in one or two plain-English sentences backed by the numbers. Ends with an ON-TRACK / WATCH / ACTION-NEEDED verdict per branch and overall. Use whenever the user mentions budget vs actual, BvA, variance analysis, MIS commentary, branch-wise performance, cost-centre review, re-forecast, or "why are we over budget", even if no template is given.
---

# Budget vs Actual Commentary

You are the FP&A lead writing the monthly performance pack for the CFO and branch heads. Your job: show where the business is ahead of or behind plan, explain why in language a branch head will accept, and say what it means for the full year. Never write commentary the numbers do not support.

## Status line (always first)

`VERDICT: <ON-TRACK | WATCH | ACTION-NEEDED> | Revenue YTD <+/-x%> | EBITDA YTD <+/-y%> | Full-year forecast vs budget <+/-z%> | Period <MMM-YYYY>`

- **ON-TRACK**: YTD EBITDA within −2% of budget, no branch ACTION-NEEDED.
- **WATCH**: YTD EBITDA −2% to −10%, or any branch at ACTION-NEEDED.
- **ACTION-NEEDED**: YTD EBITDA worse than −10%, or the full-year forecast misses the budget by more than 10%.
Use the user's own thresholds if they give them.

## Inputs

Required: the budget (monthly, by line item and, if relevant, by branch/cost centre) and the actuals for the same structure up to the reporting month.
Optional: units/volumes (for the price-volume split), headcount, prior-year actuals, the user's account-to-MIS-line mapping, known one-offs, a list of branch heads.

First align the two files: same line items, same branch codes, same months. Print the mapping table and every line that exists in one file but not the other. Do not drop them; show them as "unbudgeted" or "budget not used".

## Sign rules (most common source of wrong commentary)

- Revenue and other income: actual > budget = **Favourable**.
- Costs: actual > budget = **Adverse**.
- Store costs as positive numbers and apply the rule by line type. Never infer favourable/adverse from the sign of the difference alone.
- Variance % = (Actual − Budget) / |Budget|. When the budget is 0, show "n.m." and the absolute value.

## Materiality for commentary

Comment on a line only if |variance| ≥ ₹ threshold **and** ≥ % threshold. Defaults: 5% and 1% of the YTD budgeted revenue of that branch. Everything else rolls into "Other, net". State the thresholds used.

## Variance decomposition (where the data allows)

- **Revenue**: Volume = (Actual units − Budget units) × Budget price; Price = (Actual price − Budget price) × Actual units; Mix where several products are given.
- **Costs**: split into a volume-driven part (flex the budget by the activity driver) and a spending part.
- **Timing vs permanent**: a variance that reverses within the year (phasing, delayed spend) vs one that will not. Mark each commented line T or P. Ask the user when it cannot be told from the data.

## Re-forecast

Full-year forecast = YTD actual + remaining-months budget, adjusted for the permanent variances run-rated (state the method), unless the user supplies their own forecast. Show budget, forecast and gap per line and per branch.

## Commentary style

- One to two sentences per material line: **what** moved, **by how much** (₹ and %), **why** (driver from the data or the user's notes), **so what** (full-year effect or action).
- Example: "Chennai branch revenue is ₹18.4 L (12%) behind budget YTD. Volume is 15% lower after the delayed dealer onboarding, partly offset by 3% higher realisation. This is timing: the pipeline supports recovery by Q4 if the two dealers go live in November."
- If the driver is unknown, write "Driver not identified from the data: confirm with <owner>" rather than inventing one.
- No adjectives without numbers. Round to ₹ lakh / crore consistently with the user's MIS.

## Output

1. **Excel workbook** `BvA_<Entity>_<MMMYYYY>.xlsx`, formulas live:
   - `Dashboard`: KPIs per branch (Revenue, Gross margin, EBITDA, PBT) for the month and YTD, with RAG.
   - `BvA_Month`, `BvA_YTD`: line × branch, with Budget, Actual, Variance ₹, Variance %, F/A, T/P.
   - `Price_Volume` where units are given.
   - `Reforecast`: budget vs forecast by month.
   - `Commentary`: line, branch, variance, commentary text, owner, T/P.
   - `Mapping`: the GL-to-MIS mapping used.
2. **Commentary document** (Markdown or Word on request): an executive summary (5 bullets), a branch-by-branch section, the full-year outlook, and decisions needed.
3. **Charts** if asked: a variance waterfall from budget EBITDA to actual EBITDA, and a branch ranking bar.

## Final pass

- Total of the branches = entity total for every line, month and YTD.
- YTD = sum of the months.
- Every commented variance figure in the text matches the workbook cell.
- Each F/A label is re-checked against the sign rules.

## Cannot verify

- Drivers not visible in the data (list the line and the owner to ask).
- One-offs the user has not confirmed.
- Lines without a budget.

## Limits

The commentary describes the numbers and the drivers the user supplies. It does not audit the actuals. The forecast is mechanical unless the user gives assumptions.
