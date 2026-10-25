---
description: Prepare the NCD interest payout register with TDS and Reg 57 intimation
argument-hint: "[benpos file] [ISIN and payment date]"
---

# /ncd-interest

Load the `ncd-interest-register` skill and follow its workflow.

Input: $ARGUMENTS

If the input is missing, ask for it before starting. Read the trust deed terms, compute holder-wise interest and TDS, produce the payout file, entries and the Reg 57 draft.
