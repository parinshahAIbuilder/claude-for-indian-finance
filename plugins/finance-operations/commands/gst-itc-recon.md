---
description: Reconcile the purchase register with GSTR-2B and decide how much ITC to claim
argument-hint: "[purchase register] [GSTR-2B file]"
---

# /gst-itc-recon

Load the `gstr2b-itc-reconciler` skill and follow its workflow.

Input: $ARGUMENTS

If the input is missing, ask for it before starting. Reconcile, quantify ITC at risk, draft vendor follow-ups and give the GSTR-3B verdict.
