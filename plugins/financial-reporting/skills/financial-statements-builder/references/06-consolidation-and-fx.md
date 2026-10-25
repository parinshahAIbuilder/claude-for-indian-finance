# 06 — Consolidation, eliminations and multi-currency

## Scope
- Subsidiaries (control — Ind AS 110 / IFRS 10 / ASC 810 VIE & voting models; AS 21 for Div I):
  full consolidation line by line.
- Associates (significant influence, typically 20–50%) and joint ventures: equity method (Ind AS
  28 / IAS 28 / ASC 323; AS 23 / AS 27 for Div I).
- Joint operations: share of assets, liabilities, income, expenses.
- Companies Act s.129(3): consolidated financial statements mandatory if the company has one or
  more subsidiaries, associates or JVs; Form AOC-1 salient features statement.

## Consolidation workpaper layout (Consolidation tab)

```
FSLI | Parent | Sub A (translated) | Sub B | ... | Aggregate | Elim 1 | Elim 2 | ... | Consolidated
```
Every elimination column sums to zero (Dr = Cr). The Consolidated column feeds the consolidated
statements exactly like the standalone TB feeds standalone statements.

## Pre-consolidation steps
1. Uniform accounting policies — restate subsidiaries to group policy (e.g. local GAAP → Ind AS).
2. Uniform reporting date — if different, adjust for significant transactions (gap ≤ 3 months).
3. Translate foreign operations (below).
4. Reconcile intercompany balances: both sides must agree before elimination. Differences =
   goods/cash in transit, FX, cut-off, disputes → resolve or record adjusting entry; log in Open
   Points.

## Standard elimination entries (number them E1, E2…)

| # | Elimination | Entry |
|---|---|---|
| E1 | Investment vs equity at acquisition | Dr Share capital & pre-acquisition reserves of sub; Dr Goodwill (or Cr Capital reserve/bargain purchase); Cr Investment in sub; Cr NCI (at proportionate share or fair value — state choice) |
| E2 | Intercompany receivables/payables | Dr Payable; Cr Receivable |
| E3 | Intercompany loans and interest | Dr Borrowing; Cr Loan asset; Dr Interest income; Cr Finance cost |
| E4 | Intercompany sales/purchases | Dr Revenue; Cr Cost of sales/purchases |
| E5 | Unrealised profit in closing inventory / fixed assets | Dr Cost of sales (or retained earnings); Cr Inventory/PPE; deferred tax on the adjustment; NCI share if upstream |
| E6 | Intercompany dividends | Dr Dividend income; Cr Retained earnings (or dividend declared) |
| E7 | Intercompany management fees, rent, royalties | Dr Income; Cr Expense |
| E8 | Intercompany guarantees, corporate guarantee commission | Eliminate both sides |
| E9 | NCI share of current profit and OCI | Dr Profit attributable to NCI; Cr NCI |
| E10 | Post-acquisition reserves allocation | Track pre/post-acquisition split |

## Goodwill and NCI
- Ind AS 103 / IFRS 3: acquisition method; goodwill not amortised, tested annually for impairment
  (Ind AS 36); bargain purchase gain → OCI → capital reserve under Ind AS (to P&L under IFRS).
- AS 21: goodwill/capital reserve = cost of investment − share of equity at date of investment;
  goodwill may be amortised per policy.
- NCI presented within equity; P&L and OCI attribution to owners vs NCI shown on face.

## Multi-currency

### Functional currency
Determine per entity (Ind AS 21 / IAS 21 / ASC 830): primary economic environment — currency of
sales prices, costs, financing.

### Translation of a foreign operation into presentation currency (Ind AS 21 / IAS 21)
| Item | Rate |
|---|---|
| Assets and liabilities (incl. goodwill and FV adjustments) | Closing rate |
| Income and expenses | Rate at transaction date; average rate acceptable if not fluctuating significantly |
| Share capital and pre-acquisition reserves | Historical rate |
| Post-acquisition retained earnings | Carried forward translated amounts |
| Resulting difference | Foreign currency translation reserve (FCTR) in OCI; NCI share to NCI; recycled to P&L on disposal |
Hyperinflationary economies: apply Ind AS 29 / IAS 29 first.

### Under AS 11 (Div I)
Integral vs non-integral foreign operation; non-integral → closing rate for B/S, average for P&L,
difference to FCTR.

### Transaction-level FX (in the entity's own books)
Monetary items restated at closing rate; non-monetary at historical. Exchange differences to
P&L (except designated hedges / net investment). Make sure the TB already reflects year-end
revaluation; if not, propose an adjustment in Stage 3.

### Convenience translation
If the user wants the full set in another currency (e.g. USD for a foreign investor): translate
all figures at a single closing rate, label clearly "Convenience translation — unaudited, at
₹X = US$1 as of [date]", keep the statutory set unchanged.

### Rates
Source: RBI reference rate / FBIL for INR; central bank or the ERP's rate table. Record source,
date and rate in an FX tab; every translated cell references that tab.

## Cash flow in consolidation
Prepare from the consolidated balance sheet movement, removing FCTR and non-cash acquisition
effects; acquisition/disposal of subsidiaries shown net of cash acquired in investing; effect of
exchange rate changes on cash shown as a separate reconciling line.

## Validation specific to consolidation
- Each elimination nets to zero.
- Intercompany balances after elimination = 0 for every pair.
- Consolidated equity attributable to owners + NCI = Consolidated net assets.
- Parent's standalone profit + share of subs' post-acquisition profit ± eliminations = consolidated
  profit attributable to owners (reconciliation shown).
- FCTR movement = translation difference computed independently.
