# 02 — Ledger classification and grouping

Grouping is where most financial statements break. Treat it as an audited process, not a lookup.

## Mapping hierarchy (apply in order, record which rule decided)

| Priority | Signal | Confidence if it decides |
|---|---|---|
| 1 | User-supplied or prior-year audited mapping | High |
| 2 | ERP account type (Asset/Liability/Equity/Income/Expense + sub-type) and parent group | High if consistent with name |
| 3 | Ledger name semantics (keyword dictionary below) | Medium |
| 4 | Transaction nature: counterparty type, tax code, voucher type, recurrence | Medium → High when it corroborates 2 or 3 |
| 5 | Balance sign behaviour | Low on its own — used to challenge, not to decide |

Where signals conflict (e.g. ERP type "Expense" but name "Security Deposit Paid"), use the
substance, assign Medium/Low, and log it in Open Points.

## Mapping table schema

```
ledger_code | ledger_name | closing | fsli | note_no | sub_note | current_noncurrent |
cash_flow_bucket | rule_used | confidence | rationale | reviewer_override
```

`cash_flow_bucket` ∈ {Cash, Operating-WC, Operating-NonCash, Investing, Financing, Equity, Tax, PL}.
Assign it at mapping time — this is what makes the cash flow statement formula-driven.

## Keyword dictionary (extend per sector)

| FSLI | Keywords / signals |
|---|---|
| Property, plant and equipment | building, plant, machinery, furniture, computer, vehicle, office equipment, leasehold improvement, fit-out |
| Capital work-in-progress | CWIP, under construction, capital advance (→ other non-current assets, not CWIP) |
| Right-of-use assets | ROU, right of use, lease asset |
| Intangible assets | software, licence, trademark, goodwill, brand, customer list |
| Investments | shares in, MF, mutual fund, bonds, FD > 12 months (→ other financial assets), units |
| Trade receivables | debtors, customer names, sundry debtors, receivable, unbilled (→ contract asset / other financial asset under Ind AS) |
| Cash and cash equivalents | cash in hand, bank current a/c, FD ≤ 3 months original maturity |
| Other bank balances | FD 3–12 months, earmarked/unpaid dividend a/c, margin money |
| Loans / other financial assets | security deposit, staff advance, interest accrued, loans to related parties |
| Other current assets | prepaid, GST/VAT input credit, advance to suppliers, balance with government authorities |
| Equity share capital | share capital, equity shares |
| Other equity | reserves, securities premium, retained earnings, general reserve, OCI reserve, ESOP reserve, share application money pending allotment |
| Borrowings | term loan, NCD, debentures, OD, CC, working capital, ECB, vehicle loan, loan from director |
| Lease liabilities | lease liability |
| Trade payables | creditors, vendor names, sundry creditors, payable for expenses |
| Other financial liabilities | interest accrued, deposits received, capital creditors, unpaid dividend, employee dues |
| Provisions | gratuity, leave encashment, warranty, provision for |
| Other current liabilities | statutory dues (TDS, GST output, PF, ESI, PT), advance from customers, deferred revenue |
| Revenue from operations | sales, service income, rent income (if core), subscription |
| Other income | interest income, dividend, profit on sale of assets, FX gain, misc income |
| Employee benefits expense | salary, wages, bonus, PF contribution, gratuity, staff welfare, ESOP cost |
| Finance costs | interest on loans/NCD/lease liabilities, processing fees (amortised), bank charges on borrowings |
| Depreciation and amortisation | depreciation, amortisation |
| Other expenses | everything else, sub-grouped in the note (rent, power, repairs, legal, auditor's remuneration, CSR, etc.) |
| Tax | current tax, deferred tax, MAT, income tax provision, advance tax (→ net against provision by jurisdiction) |

## Transaction-nature rules (use the GL when available)

- Ledger receiving GST/VAT *output* tax lines on credit side → revenue or advance from customers.
- Ledger receiving TDS 194I (rent) deductions → rent expense; 194C → contract services;
  194J → professional fees; 192 → salary; 194A → interest expense.
- Fixed monthly debit to a bank-linked party with interest component → loan EMI; split principal
  (financing) and interest (finance cost).
- Party appearing in both debtor and creditor ledgers → flag for netting review (net only where a
  legal right of set-off exists).
- Ledger with entries only from group entities → intercompany; tag for elimination and RPT.
- Round-sum journals on the last day with no counterparty → potential provision or plug — flag.

## Mandatory challenges (run on every mapping)

1. **Sign anomalies**: debit-balance creditors → reclassify to advances; credit-balance debtors →
   reclassify to advances from customers; credit-balance bank → borrowings (OD); negative fixed
   assets → error.
2. **Suspense / unclassified / clearing / difference in opening** ledgers with non-zero balance →
   CRITICAL open point. Never map to "Other".
3. **Duplicates**: fuzzy-match ledger names (e.g. "HDFC Bank", "HDFC Bank Ltd A/c 1234") and party
   names across groups; flag pairs above 85% similarity.
4. **Current / non-current split** for borrowings, deposits, provisions, lease liabilities —
   needs repayment schedules; if absent, flag and use stated assumption.
5. **Materiality of "Other expenses" sub-items**: any item > 1% of revenue or ₹10 lakh (whichever
   is higher, for Schedule III Div I) must be shown separately; for Ind AS use the entity's
   materiality judgement and disclose.
6. **Mapping completeness**: Σ mapped balances = Σ TB balances; count of mapped = count of ledgers.
