---
description: Build the dated LODR checklist for quarterly results and quarter-end filings
argument-hint: "[quarter-end date] [board meeting date]"
---

# /results-checklist

Load the `sebi-lodr-disclosure` skill and follow its workflow.

Input: $ARGUMENTS

If the input is missing, ask for it before starting. Produce the results-day and quarter-end checklist from the quarter-end and board meeting dates, covering equity and, if applicable, debt-listed obligations.
