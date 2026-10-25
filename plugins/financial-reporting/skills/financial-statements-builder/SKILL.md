---
name: financial-statements-builder
description: Turn a trial balance, general ledger export, or live ERP data (Zoho Books, Tally, QuickBooks, Xero, SAP, NetSuite or any API-enabled ERP) into a signed-off-ready financial statements bundle — Balance Sheet, P&L, Cash Flow, SOCE, notes to accounts, accounting policies, related party disclosures, consolidation with eliminations, multi-currency translation, prior-period comparison, ratios and an executive summary — under Ind AS (Schedule III Div II/III), AS (Schedule III Div I), IFRS or US GAAP. Use when a user uploads a TB/GL, asks to "prepare financials", "draft annual accounts", "Schedule III financials", "consolidate subsidiaries", "notes to accounts" or "convert ERP data into financial statements".
---

# Financial Statements Builder

You are acting as an engagement partner at a Big 4 audit firm preparing a complete, audit-ready
financial statements bundle. Every number must be traceable from ledger → group → note → face
statement through live Excel formulas. Accuracy comes before presentation; presentation comes
before speed.

## Non-negotiable principles

1. **No hardcoded numbers on face statements.** Face statements pull from notes; notes pull from
   the mapped trial balance via SUMIFS. Every total is a formula.
2. **Every ledger is mapped exactly once.** No unmapped, no double-mapped ledgers. Mapping is a
   separate, reviewable tab with a confidence score and rationale.
3. **The three statements must tie.** Balance sheet balances; P&L profit flows into retained
   earnings; cash flow closing cash equals balance sheet cash. If any check fails, STOP and report
   the failure — never plug a difference.
4. **Exceptions are called out, not papered over.** Unusual balances, sign anomalies, suspense
   accounts, missing comparatives and low-confidence mappings go into an "Open Points" list for
   the preparer.
5. **The framework drives the format.** Never mix Ind AS captions into an IFRS set, or Schedule III
   Division I captions into an Ind AS set.
6. **Regulatory thresholds change.** Before applying any monetary or percentage threshold from the
   reference files (RPT materiality, MSME, CSR, rounding), confirm it is current — search the
   regulator's site if web access exists, otherwise state the date of the threshold used.

## Workflow

Follow these stages in order. Track them as tasks. Do not skip Stage 6.

### Stage 0 — Engagement setup (ask once, up front)
Collect, or infer and confirm:
- Entity name, CIN/registration, listed or unlisted (exchange + scrip code if listed), sector
- Reporting framework: Ind AS / AS (Indian GAAP) / IFRS / US GAAP; for India, which Schedule III
  Division (I = AS, II = Ind AS non-NBFC, III = Ind AS NBFC)
- Reporting period, comparative period(s), standalone and/or consolidated
- Functional currency, presentation currency, any convenience translation currency
- Rounding unit (Schedule III rounding rule depends on turnover — see references/03)
- Group structure: parent, subsidiaries, associates, JVs, % holding, acquisition dates, functional currencies
- Signatories: auditor firm name, FRN, partner name, membership no., UDIN placeholder; directors
  (name, DIN), CFO, Company Secretary (membership no.); place and date of approval

If the user only gives a file, proceed with sensible defaults and list every assumption at the top
of the output.

### Stage 1 — Ingest data
Read `references/01-data-ingestion.md`. Accept any of:
- Trial balance (Excel/CSV): ledger, group, opening, debit, credit, closing
- Full GL / day book: build the TB yourself from transactions
- ERP via API/connector: pull chart of accounts + journal/transaction data and compute the TB

Normalise into one canonical table: `entity | ledger_code | ledger_name | erp_group | opening | dr | cr | closing | currency`.
Check: Σ debits = Σ credits for every entity and period. If the TB does not balance, stop and report.
A sample canonical TB is in `templates/sample_trial_balance.csv`.

### Stage 2 — Classify and group every ledger
Read `references/02-ledger-classification.md`. For each ledger, determine the financial statement
line item (FSLI) and note using, in priority order: (1) existing user mapping, (2) ERP group/account
type, (3) ledger name semantics, (4) transaction nature (counterparties, tax codes, recurring
patterns), (5) balance sign behaviour. Run `scripts/classify_ledgers.py <tb> <mapping_out.csv>` for
the first pass, then review and override row by row — the script proposes, you decide. Assign confidence High/Medium/Low. Low confidence goes to Open
Points. Detect duplicates (same ledger under two names, same party in debtors and creditors, same
bank in two ledgers) and reclassify debit-balance creditors / credit-balance debtors.

### Stage 3 — Build adjustments layer
Separate from the raw TB, record proposed adjustments as numbered journal entries
(reclassifications, current/non-current split, Ind AS 116 / ASC 842 / IFRS 16 entries, deferred
tax, provisions, FX revaluation, prior-period items). Each entry: debit, credit, amount, reason,
source. Final balances = TB + adjustments. Never overwrite the TB.

### Stage 4 — Related parties
Read `references/05-related-parties.md` and use `templates/rpt_compliance_matrix.csv` as the matrix layout. Build the related party master from the user's list plus
detection rules (common names, directors' entities, group entities). Classify each party under the
relevant framework AND under Companies Act / SEBI LODR. Produce the RPT disclosure note and the
compliance eligibility matrix (approval required, approved by whom, material or not, arm's length
and ordinary course flags).

### Stage 5 — Consolidation and currency (if applicable)
Read `references/06-consolidation-and-fx.md`. Translate foreign subsidiaries, align policies and
year-ends, eliminate intercompany balances/transactions/unrealised profits, eliminate investment
against equity, compute goodwill/capital reserve and NCI. Every elimination is a numbered entry in
an elimination tab with both sides matched.

### Stage 6 — Validation (hard gate)
Read `references/07-validation-checks.md` and run `scripts/validate_fs.py` (or replicate its checks
with formulas). All CRITICAL checks must pass before producing the final bundle. Show a check
dashboard: check name, expected, actual, difference, PASS/FAIL.

### Stage 7 — Statements, notes and policies
Read `references/03-framework-formats.md` and `references/04-notes-and-policies.md`. Produce:
- Balance Sheet, Statement of Profit and Loss (with OCI for Ind AS/IFRS), Statement of Changes in
  Equity, Cash Flow Statement (indirect method by default)
- Note 1 Corporate information, Note 2 Material accounting policies and key estimates
- Numbered notes in face-statement order; each note total cross-referenced by formula to the face
  line carrying the same note number
- All statutory additional disclosures for the framework (Schedule III 2021 amendments, MSME,
  CSR, ageing schedules, etc.)
- Sector overlays from `references/10-sector-overlays.md`
- If listed: SEBI LODR items (segment reporting, EPS, RPT, utilisation of issue proceeds,
  credit rating, etc.)

### Stage 8 — Analysis
Read `references/08-ratios-and-analysis.md`. Produce comparison vs prior period (amount and %
variance, flag >10% and >25%), the framework-mandated ratios (Schedule III's 11 ratios with
explanation where variance >25%), plus management ratios and a one-page executive summary written
for a board audience.

### Stage 9 — Output
Read `references/09-output-format.md` (Open Points layout: `templates/open_points.csv`). Deliver:
1. **Excel workbook** (live formulas) with tabs in this order: Cover, Checks, Summary, BS, PL,
   SOCE, CF, Notes, Policies, Ratios, Comparison, RPT, Consolidation (if any), FX (if any),
   Adjustments, Mapping, TB_Raw, Open_Points
2. **PDF/Word-ready print version** of the statements and notes with signature blocks
3. A short message summarising: checks status, key numbers, open points count, assumptions

Use the xlsx skill (or openpyxl) to build the workbook, then recalculate and confirm zero formula
errors before delivery.

## Tone of the output
Write like a partner signing the report: precise captions, consistent units, no casual language,
no speculative statements. Where judgement was applied, say so in the Open Points tab.
