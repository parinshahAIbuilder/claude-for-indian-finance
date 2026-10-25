---
description: Run the month-end close gate: TB checks, bank reconciliation, TDS and MSME payables
argument-hint: "[period] [trial balance]"
---

# /month-end-close

Load the `trial-balance-close-gate` skill and follow its workflow.

Input: $ARGUMENTS

If the input is missing, ask for it before starting. Run the close gate, then use bank-reconciliation-brs, tds-compliance-auditor and msme-43bh-payables-gate for the items it flags. Finish with a close sign-off summary.
