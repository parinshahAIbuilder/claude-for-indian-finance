# 07 — Validation checks (hard gate)

Run all checks; build them as live formula cells on the **Checks** tab so they re-evaluate when
anything changes. A CRITICAL failure blocks delivery of the final bundle — report it and stop.
WARNING failures are delivered with the bundle and listed in Open Points.

Tolerance: 0 for formula-driven checks; ≤ 1 rounding unit only where rounding is applied after
aggregation (state it).

| # | Check | Severity | Formula logic |
|---|---|---|---|
| C01 | TB balances | CRITICAL | Σ closing (Dr +, Cr −) = 0, per entity |
| C02 | Opening TB = prior closing TB | CRITICAL | Ledger-wise difference = 0 (after prior audit adj.) |
| C03 | Roll-forward per ledger | CRITICAL | opening + Dr − Cr − closing = 0 |
| C04 | All ledgers mapped | CRITICAL | COUNTBLANK(Mapping[fsli]) = 0 |
| C05 | No ledger double-mapped | CRITICAL | COUNTIF(ledger_code) = 1 for every code |
| C06 | Mapped total = TB total | CRITICAL | Σ Mapping balances − Σ TB = 0 |
| C07 | Balance sheet balances | CRITICAL | Total assets − (Equity + Liabilities) = 0, both periods |
| C08 | P&L → equity link | CRITICAL | Closing retained earnings − (opening + profit for the year − dividends ± other transfers) = 0 |
| C09 | OCI → reserves link | CRITICAL | OCI for the year = movement in OCI reserves in SOCE |
| C10 | Cash flow closing cash = BS cash and cash equivalents | CRITICAL | Incl. bank OD treated as cash where policy says so — reconcile |
| C11 | Cash flow opening cash = prior BS cash | CRITICAL | |
| C12 | Net change in cash = CFO + CFI + CFF + FX effect | CRITICAL | |
| C13 | Every note total = face line with same note number | CRITICAL | One check per note, both periods |
| C14 | SOCE closing = BS equity | CRITICAL | Per component |
| C15 | PPE roll-forward | CRITICAL | Opening + additions − disposals = closing gross; same for acc. dep.; dep. charge in note = P&L dep. |
| C16 | Depreciation in CF add-back = P&L | CRITICAL | |
| C17 | Tax: P&L tax = current + deferred; deferred movement = DTA/DTL movement (P&L portion) | CRITICAL | |
| C18 | Eliminations net to zero; IC balances = 0 post-elim | CRITICAL | Consolidation only |
| C19 | No #REF!, #DIV/0!, #VALUE!, #N/A anywhere | CRITICAL | After recalculation |
| C20 | Suspense / unclassified ledgers = 0 | CRITICAL | Or explicitly approved by user with explanation |
| C21 | Sign anomalies reclassified | WARNING | Debit creditors, credit debtors, credit bank |
| C22 | Low-confidence mappings reviewed | WARNING | Count of Low = items in Open Points |
| C23 | Duplicate ledger / party suspects | WARNING | Fuzzy match ≥ 85% |
| C24 | Comparatives tie to prior-year audited FS | WARNING | After regrouping; disclose regrouping |
| C25 | EPS recomputes | WARNING | Profit attributable ÷ weighted shares |
| C26 | Ratio inputs reference face statements | WARNING | No hardcodes in Ratios tab |
| C27 | Ageing schedules total = note balances | WARNING | Receivables, payables, CWIP |
| C28 | MSME dues in payables note = MSME disclosure | WARNING | |
| C29 | RPT note balances = balances in respective notes | WARNING | |
| C30 | Rounding: face totals = sum of rounded lines (or rounding difference disclosed) | WARNING | |
| C31 | Effective tax rate reconciliation ties to tax expense | WARNING | |
| C32 | Analytical: line movement > 25% without commentary | WARNING | Feeds Comparison tab |

## Error-mitigation techniques (use all)
- **Formula, not values**: every derived cell is a formula; inputs live only in TB_Raw,
  Adjustments, Mapping and FX tabs (blue font), formulas black, cross-sheet links green.
- **SUMIFS by note_no**, never manual SUM ranges that miss inserted rows.
- **Duplicate detection** on vouchers (same date, amount, party, voucher number) when a GL is
  provided — flag possible double-postings.
- **Benford / round-amount scan** on manual journals near period end — flag, don't conclude.
- **Independent recomputation**: cash flow built from balance sheet movements AND checked
  against the bank ledgers' total receipts/payments where GL is available.
- **Second-pass review**: after building, re-read the face statements as a reviewer — captions
  in the right framework, units consistent, note numbers ascending, no orphan notes.

## Script
`scripts/validate_fs.py` runs C01–C08, C10, C13 and C19 on the produced workbook (reads values
after LibreOffice recalculation). Run it; paste its output summary into the Checks tab or the
final message.
