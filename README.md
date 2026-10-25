# Claude for Indian Finance

**Claude plugins for Indian finance, accounts and listed-company compliance.** SEBI LODR, Ind AS, GST, TDS, CMA, NCDs and credit ratings, packaged as ready-to-install Claude Code / Cowork plugins.

[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
![Skills](https://img.shields.io/badge/skills-17-D97757)
![Plugins](https://img.shields.io/badge/plugins-4-blue)
![Made for India](https://img.shields.io/badge/made%20for-India-138808)

Anthropic's [financial-services plugins](https://github.com/anthropics/financial-services-plugins) cover DCF, comps and LBOs for global markets. None of it knows what a Reg 30 disclosure, a GSTR-2B mismatch, Form V MPBF or a section 193 TDS deduction is. This repository fills that gap, written by a practising listed-company CFO (CA, CPA) who has taken a company from startup to a main board IPO on NSE and BSE.

## Install

In Claude Code or Cowork:

```
/plugin marketplace add parinshahAIbuilder/claude-for-indian-finance
```

Then install the plugins you need:

```
/plugin install listed-company-cfo@claude-for-indian-finance
/plugin install financial-reporting@claude-for-indian-finance
/plugin install finance-operations@claude-for-indian-finance
/plugin install debt-and-treasury@claude-for-indian-finance
```

Using claude.ai instead? Zip any folder under `plugins/<plugin>/skills/` and upload it under Settings → Capabilities → Skills.

## What's inside

### Listed Company CFO

| Skill | What it does | Command |
|---|---|---|
| sebi-lodr-disclosure | Reg 30 classification, materiality test, disclosure clock and BSE / NSE intimation; results-day and quarter-end LODR checklist | `/reg30`, `/results-checklist` |
| ipo-offer-document-review | Forensic DRHP / RHP review against SEBI ICDR, LODR, Companies Act, Schedule III and Ind AS | `/review-drhp` |
| annual-report-review | Pre-signing annual report review: casting, note tie-out, CARO, Schedule III and SEBI disclosures | `/review-annual-report` |
| review-markup | Puts findings into the client's own files: PDF highlights, Word tracked changes, Excel cell marking | |

### Financial Reporting

| Skill | What it does | Command |
|---|---|---|
| financial-statements-builder | Trial balance or ERP data to audit-ready statements with notes, RPT, consolidation and ratios (Ind AS, AS, IFRS, US GAAP) | `/build-financials` |
| ind-as-116-leases | Lease register, ROU and liability schedules (with a Python calculator), entries, deferred tax, modifications and the Ind AS to IGAAP bridge | `/ind-as-116` |

### Finance Operations

| Skill | What it does | Command |
|---|---|---|
| gstr2b-itc-reconciler | Purchase register vs GSTR-2B / IMS, ITC at risk, vendor follow-ups, GSTR-3B verdict | `/gst-itc-recon` |
| tds-compliance-auditor | TDS deduction, rate and deposit checks across sections | |
| msme-43bh-payables-gate | MSME payables beyond 45 days and the section 43B(h) disallowance | |
| bank-reconciliation-brs | Bank reconciliation with ageing of unreconciled items | |
| trial-balance-close-gate | Month-end close gate on the trial balance | `/month-end-close` |
| budget-vs-actual-commentary | Variance analysis with board-ready commentary | |
| receivables-ageing-ecl | Receivables ageing and Ind AS 109 expected credit loss | |
| journal-entry-red-flag-scanner | Journal entry testing for audit red flags | |

### Debt & Treasury

| Skill | What it does | Command |
|---|---|---|
| cma-bank-loan | CMA Forms I–VI, MPBF (Tandon / Nayak / cash budget), drawing power, term loan DSCR, lender note | `/cma` |
| ncd-interest-register | Holder-wise NCD interest from benpos, day count per trust deed, section 193 / 197 / 206AA / 195 TDS, payout file, Reg 57 | `/ncd-interest` |
| dscr-credit-rating | DSCR, ISCR, net debt / EBITDA, covenant headroom, rating information pack, presentation and Q&A | `/rating-pack` |

## Who it is for

CFOs, financial controllers, company secretaries, chartered accountants, audit teams, treasury and FP&A teams at Indian listed and unlisted companies, and the CA firms and advisers who serve them.

## Important

These skills help a qualified professional work faster. They are not legal, tax or investment advice. SEBI, MCA, CBDT and GST rules change often: every skill tells Claude to flag timelines and rates that must be confirmed against the latest notification before filing.

## Standalone repos

Some skills also live in their own repos with more documentation: [indian-compliance-calendar](https://github.com/parinshahAIbuilder/indian-compliance-calendar) (full Node.js compliance app), [ipo-offer-document-review](https://github.com/parinshahAIbuilder/ipo-offer-document-review), [annual-report-review](https://github.com/parinshahAIbuilder/annual-report-review), [financial-statements-builder](https://github.com/parinshahAIbuilder/financial-statements-builder), [india-finance-agent-skills](https://github.com/parinshahAIbuilder/india-finance-agent-skills), [review-markup](https://github.com/parinshahAIbuilder/review-markup).

## Roadmap

- Tally Prime workflows (close, GSTR-2B matching, ageing)
- GST and income-tax notice replies
- Board pack and investor presentation builder

## Companion: Indian legal

For contracts, leases, SHA / ESOP documents, Companies Act resolutions and FEMA / RBI compliance, use [Claude for Legal: India Edition](https://github.com/parinshahAIbuilder/claude-for-legal-india):

```
/plugin marketplace add parinshahAIbuilder/claude-for-legal-india
```

Ideas and pull requests are welcome: see [CONTRIBUTING](CONTRIBUTING.md). If this saves your team time, a ⭐ helps other finance teams find it.

## Author

[Parin Shah](https://www.linkedin.com/in/parinshah-cfo), CFO | CA (ICAI) | CPA (AICPA). MIT licensed.
