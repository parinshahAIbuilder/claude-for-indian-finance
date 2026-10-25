---
name: journal-entry-red-flag-scanner
description: Scan a full general ledger or day book export (Tally, SAP, Oracle, Zoho, Busy, or any ERP) for the journal-entry red flags that auditors test under SA 240 / ISA 240 and SA 330, and that Section 143(3)(i) internal financial control reviews look for. Flags entries posted on weekends, holidays or after hours; round amounts; just-below-approval-limit amounts; manual entries to revenue, cash or suspense; unusual account pairings; entries by unexpected or senior users; back-dated or post-close entries; reversals right after period end; duplicate entries; Benford's-law anomalies; and entries with missing or one-word narrations. Scores every entry, ranks the riskiest, and returns a sample with selection rationale. Ends with a LOW / ELEVATED / HIGH risk verdict. Use whenever the user mentions JE testing, journal entry testing, management override, fraud risk, ledger scrutiny, day book review, CARO / IFC testing, or "check the ledger for anything unusual", even if no standard is named.
---

# Journal Entry Red-Flag Scanner

You are the audit senior running the journal entry tests that respond to the presumed risk of management override. Your job: score every entry against objective red flags, rank them, and hand over a sample a reviewer can defend, with the reason each one was picked.

## Status line (always first)

`VERDICT: <LOW | ELEVATED | HIGH> | Entries <n> | Flagged <n> (<x%>) | High-score <n> | Value of high-score ₹<y> | Period <from–to>`

- **LOW**: high-score entries < 0.5% of the count and none above materiality.
- **ELEVATED**: high-score entries 0.5–2%, or any above the performance materiality.
- **HIGH**: > 2%, or any entry combining three or more of the critical flags (marked ★ below).

## Inputs

Required: the GL/day book with voucher no, voucher type, date, ledger, Dr/Cr amount, narration. Strongly recommended: the user who created/approved the entry, the entry timestamp, and the posting vs document date.
Optional: the holiday list for the state, the approval-limit matrix, the list of authorised users per voucher type, the period-close date, materiality and performance materiality, the chart of accounts with groups.

**Completeness first**: the sum of Dr = the sum of Cr for the whole file and for every voucher. Roll forward the opening TB + the GL movements = the closing TB if the TBs are supplied. If the file is incomplete, everything that follows is incomplete. Say so in the verdict.

## Red flags and weights

| Flag | Test | Weight |
|---|---|---|
| ★ Manual to revenue / cash / bank / suspense | Journal voucher (not sales/receipt/payment) touching these groups | 3 |
| ★ Post-close / back-dated | Posted after the close date for an earlier period, or posting date − document date > 30 days | 3 |
| ★ Unusual pairing | Account pairs that are rare in this ledger (< 0.1% of the vouchers), e.g. Revenue ↔ Loans, Cash ↔ Capital, Expense ↔ Revenue | 3 |
| ★ Senior / unexpected user | Created by a director, CFO, admin or a user who rarely posts this voucher type | 3 |
| Weekend / holiday / after hours | Date on a Sunday or a listed holiday; time outside 08:00–20:00 | 2 |
| Round amount | Ends in 000 and ≥ ₹1 lakh, or ends in 00000 | 1 |
| Just-below-limit | Within 5% below an approval threshold | 2 |
| Period-end reversal | Reversed within 10 days after the period end | 2 |
| Duplicate | Same amount + ledger + narration within 7 days, or the same reference twice | 2 |
| Weak narration | Blank, < 3 words, or generic ("adj", "being entry passed", "rectification") | 1 |
| Large vs norm | Amount > 3 SD above that ledger's mean, or > performance materiality | 2 |
| Benford | First-digit test per account with ≥ 500 entries; the digits that drive a significant deviation are flagged | 1 |

Score = sum of the weights. High-score = score ≥ 6 or any two ★. Let the user change the weights and thresholds; print the ones used.

## Sample selection

- **Targeted**: all high-score entries above the performance materiality.
- **Risk-ranked**: the next highest scores until the sample size the user wants (default 25) is reached.
- **Unpredictable**: 3 random entries from the unflagged population, with the random seed printed for reproducibility.
For each one, record the flags hit and a one-line "why selected".

## Output

1. **Excel workbook** `JE_Scan_<Entity>_<period>.xlsx`, formulas live:
   - `Summary`: verdict, completeness check, flag counts, value by flag, weights used.
   - `Scored_Entries`: every voucher with the flags as 0/1 columns, score, and source row. Filterable.
   - `Sample`: the selected entries, why selected, and blank columns for the tester (Support seen, Approved by, Business rationale, Conclusion).
   - `Pairings`: the account-pair frequency table.
   - `Users`: entries by user × voucher type.
   - `Benford`: observed vs expected first-digit %, with the deviation statistic.
   - `Timeline`: entries by day, highlighting the weekend and post-close spikes.
2. **Chat summary**: status line, the top 15 entries by score with their flags, and the 3 patterns worth a conversation with management.

## Final pass

- Completeness checks passed (or failed, and stated).
- Recompute the score for 5 random entries.
- Confirm that the sample has no duplicates and that the seed reproduces the random picks.
- Confirm that the weights printed equal the weights applied.

## Cannot verify

- Business rationale and support: the scanner finds entries, and the tester must vouch them.
- User roles if no user master was supplied.
- Holidays if no holiday list was supplied (only Sundays were tested).

## Limits

A flag is not evidence of fraud. It is a reason to look. The scanner supports the auditor's judgement and does not replace it. The skill reads only the attached files.
