# 01 — Data ingestion

## Accepted inputs

| Input | Minimum columns | Notes |
|---|---|---|
| Trial balance | Ledger name, closing balance (Dr +ve / Cr −ve, or separate Dr/Cr columns) | Ask for opening balances too — needed for cash flow and SOCE |
| TB with groups | + ERP group / parent group / account type | Use as a strong mapping signal, never as final truth |
| General ledger / day book | Date, voucher no., voucher type, ledger, Dr, Cr, narration, party | Build TB by aggregation; keep vouchers for nature analysis |
| Prior-year audited FS | PDF or Excel | Used for comparatives and to learn prior mapping |
| Fixed asset register | Asset class, cost, additions, disposals, depreciation | Feeds PPE note |
| Party ledgers / ageing | Party, invoice date, due date, outstanding | Feeds receivable/payable ageing |
| Related party list | Name, relationship, PAN/registration | Seeds RPT master |

## Canonical schema (normalise everything into this)

```
entity | period | ledger_code | ledger_name | erp_group | erp_account_type |
opening_balance | period_debit | period_credit | closing_balance | currency
```

Sign convention: debit positive, credit negative. Convert "Cr" suffixes, brackets and minus
signs consistently. Strip thousand separators and Indian-format commas (1,23,45,678).

## Integrity checks on ingestion
- Σ closing_balance = 0 per entity (TB balances). Tolerance: ≤ 1 unit of smallest currency.
- opening_balance + period_debit − period_credit = closing_balance per ledger.
- Opening TB of current year = closing TB of prior year (after prior-year audit adjustments).
- No blank ledger names; no duplicate ledger codes.
- Opening retained earnings = prior closing retained earnings + prior-year profit transfer
  (some ERPs keep P&L ledgers open — detect and roll forward).

## ERP connectors (pull data, compute TB yourself)

Prefer a connector or API over asking the user for exports. General pattern:
1. Pull chart of accounts (codes, names, account types, parent groups).
2. Pull all posted transactions/journals for the period plus opening balances.
3. Aggregate to TB; reconcile against the ERP's own TB report if available.

| ERP | Route |
|---|---|
| Zoho Books | Chart of accounts and account-level transactions via the Books API (`/chartofaccounts`, account transactions, journals); organization settings for base currency and fiscal year. Use a connector if one is attached. |
| Tally Prime / ERP 9 | XML/HTTP requests to the Tally server port (default 9000) using TDL "Trial Balance" / "Ledger" collections, or ODBC |
| QuickBooks Online | Reports API — TrialBalance and GeneralLedger reports; Accounts query |
| Xero | Accounting API — Reports/TrialBalance, Accounts, Journals |
| SAP S/4HANA | OData services for G/L account balances and journal entry items |
| Oracle NetSuite | SuiteQL / REST on transaction and account records |
| Microsoft Dynamics 365 BC | REST API trialBalance and generalLedgerEntries |
| Any other | Ask for an API spec or a GL export in the canonical schema |

Never write data back to the ERP. This skill is read-only on source systems.

## What to capture from transactions (for classification in stage 2)
- Counterparty type (customer, vendor, employee, bank, government, group entity)
- Tax codes (GST/VAT input vs output, TDS/withholding sections) — strong signal of nature
- Voucher types (payment, receipt, journal, sales, purchase, contra)
- Recurrence and timing (monthly fixed amounts → rent, salary, EMI, interest)
- Narration keywords
