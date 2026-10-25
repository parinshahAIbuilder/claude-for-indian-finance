# 05 — Related parties and RPT eligibility mechanism

Three overlapping definitions apply to an Indian listed company. Classify every party under each
one separately — a party can be related under one and not another. **Thresholds below are as
understood at the time of writing; confirm against the current Act, Rules, LODR and SEBI
circulars before applying.**

## 1. Definitions

| Source | Who is a related party (summary) |
|---|---|
| **Companies Act 2013, s.2(76)** | Director or KMP or their relative; firm in which a director/manager or relative is partner; private company in which director/manager or relative is member or director; public company in which director/manager is director AND holds (with relatives) >2% paid-up capital; body corporate whose board/MD/manager acts on the advice of a director/manager; person on whose advice a director/manager acts (except professional advice); holding, subsidiary, associate company, subsidiary of holding (fellow subsidiary); investing company or venturer; director (other than independent director) or KMP of holding company or their relative; persons prescribed in Rule 3 of Companies (Specification of Definitions Details) Rules. "Relative" per s.2(77) and Rule 4. |
| **Ind AS 24 / IAS 24** | Person or close family member with control, joint control or significant influence, or who is KMP of the entity or its parent; entities in the same group; associates and JVs (and their group members); post-employment benefit plans; entities controlled by such persons; entities providing KMP services. |
| **SEBI LODR Reg 2(1)(zb)** | Related party under Act s.2(76) or the applicable accounting standards, **plus** any person/entity in the promoter or promoter group holding ≥20% (or ≥10% from FY 2023-24 onward) of equity, directly or on beneficial-interest basis, at any time in the immediately preceding financial year. |
| **AS 18 (Div I)** | Control or significant influence relationships; KMP and relatives; enterprises over which KMP/relatives have significant influence. |
| **US GAAP ASC 850** | Affiliates, equity-method investees, trusts for employee benefits, principal owners (>10%), management and immediate families, others who can significantly influence. |

## 2. Detection rules (to build the master beyond the user's list)
- Group entities: parent, subsidiaries, associates, JVs from Stage 0 structure.
- Directors and KMP from the board composition; their known entities (MBP-1 / DIR-8 disclosures
  if provided; otherwise MCA director master search by DIN if web access exists).
- Name matching: party names sharing promoter surnames, group brand names, or registered address.
- Transaction behaviour: unsecured interest-free loans, non-standard credit terms, round-figure
  advances, rent paid to individuals → probable related party; confirm with the user.
- Promoter group holding ≥ threshold from the latest shareholding pattern (listed entities).
Every auto-detected party is "Proposed — confirm" until the user confirms.

## 3. Transaction capture
For each related party: nature of transaction (sale/purchase of goods, services, rent, loans
given/taken, interest, guarantees, remuneration, sitting fees, reimbursements, capital
infusion, dividend), amount in the period, closing balance (receivable/payable/guarantee),
terms, whether secured, provision for doubtful debts, and amounts written off.

## 4. Eligibility and approval matrix (Companies Act s.188 + Rule 15, LODR Reg 23)

For each transaction compute and record:

| Column | Logic |
|---|---|
| Covered by s.188? | Is the nature one of the 7 listed in s.188(1): sale/purchase/supply of goods or materials; sale/disposal/buying of property; leasing of property; availing/rendering services; appointment of agents; appointment to office or place of profit; underwriting of securities |
| Ordinary course of business? | Matches stated objects + regular, frequent pattern + similar with unrelated parties — judgement; record basis |
| Arm's length? | Evidence: comparable third-party prices, benchmarking, TP study; record basis |
| s.188 board approval required? | Covered AND NOT (ordinary course AND arm's length) |
| s.188 shareholder (ordinary resolution) approval required? | Board approval required AND above Rule 15(3) thresholds — e.g. goods/property sale/purchase ≥10% of turnover; leasing ≥10% of turnover; services ≥10% of turnover; office or place of profit remuneration > ₹2.5 lakh per month; underwriting > 1% of net worth (confirm current values) |
| Audit committee approval (s.177 / Reg 23(2))? | **All** RPTs and subsequent material modifications — prior approval; omnibus approval permitted for repetitive transactions within limits (Reg 23(3)) |
| Approval by independent directors only on AC? | Listed entity: only independent directors on the AC approve RPTs |
| Material RPT under LODR Reg 23(1)? | Transaction(s) with a party in the year, individually or aggregated, exceed **lower of ₹1,000 crore or 10% of annual consolidated turnover** per last audited FS; brand/royalty payments >5% of annual consolidated turnover. (SEBI has consulted on a scale-based threshold — check whether a revised framework is in force.) |
| Shareholder approval under Reg 23(4)? | Material RPT → prior approval by ordinary resolution; related parties may not vote in favour |
| Subsidiary transactions | RPTs of an unlisted subsidiary with parties of the listed entity also count where above thresholds (Reg 23 as amended) |
| Exemptions | Transactions between holding company and wholly-owned subsidiary whose accounts are consolidated (except as specified); between two WOS of the listed holding; certain government company and statutory transactions; uniform corporate actions like dividend/rights to all shareholders |
| Disclosure | Reg 23(9): half-yearly RPT disclosure to exchanges in prescribed format (now with results); Form AOC-2 in Board's report for contracts under s.188(1); Ind AS 24 note in FS; register MBP-4 |
| Status | Approved / Approval pending / Ratification needed / Non-compliant — flag for CS |

Output this as the **RPT Compliance Matrix** tab with conditional formatting: red where approval
is required but not evidenced. This is a compliance aid, not a legal opinion — say so on the tab.

## 5. Financial statement note (Ind AS 24 format)
(a) Names of related parties and nature of relationship (by category: holding, subsidiaries,
fellow subsidiaries, associates/JVs, KMP, relatives of KMP, entities where KMP/relatives have
control or significant influence, post-employment plans).
(b) Transactions during the year — by nature and party, both years.
(c) Balances outstanding at year end — by nature and party, both years.
(d) KMP compensation — short-term benefits, post-employment, other long-term, termination,
share-based payment (Ind AS 24.17).
(e) Terms and conditions: arm's length, unsecured, settlement in cash, guarantees given/received.
(f) Schedule III: loans/advances to promoters, directors, KMP and related parties repayable on
demand or without specified terms — amount and % of total.
