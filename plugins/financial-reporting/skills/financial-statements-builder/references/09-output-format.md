# 09 — Output format and presentation

## Workbook (tab order)
Cover → Checks → Summary → BS → PL → SOCE → CF → Notes → Policies → Ratios → Comparison → RPT
(+ RPT_Matrix) → Consolidation → FX → Adjustments → Mapping → TB_Raw → Open_Points

## Formatting standards
- Font: Calibri/Arial 10–11; headings 12–14 bold. Entity name, statement title, date line and
  "(All amounts in ₹ lakhs unless otherwise stated)" at top of every statement page.
- Columns: Particulars | Note No. | Current period | Previous period. Note column centred.
  Amount columns right-aligned, same width, number format `#,##0.00;(#,##0.00);"-"` (Indian
  grouping `##,##,##0.00` where presentation is in absolute rupees).
- Captions: Roman numerals / letters exactly as the framework format; sub-totals single top
  border; grand totals single top + double bottom border, bold.
- Colour coding (model tabs): inputs blue, formulas black, cross-sheet links green; check cells
  green fill on PASS, red on FAIL via conditional formatting.
- Freeze panes at header row; print area set; fit to 1 page wide; landscape for roll-forwards.
- No merged cells inside numeric areas (breaks formulas and sorting).
- Negative numbers in brackets; zero shown as "-".
- Every note page header repeats the note number and title.

## Signature block (bottom of BS, PL, SOCE, CF)

```
The accompanying notes form an integral part of the financial statements.

As per our report of even date                For and on behalf of the Board of Directors of
For [Audit Firm Name]                         [Company Name]
Chartered Accountants                          CIN: [ ]
Firm Registration No.: [ ]

[Partner Name]                                 [Name]                 [Name]
Partner                                        Managing Director      Director
Membership No.: [ ]                            DIN: [ ]               DIN: [ ]
UDIN: [ ]
                                               [Name]                 [Name]
                                               Chief Financial Officer  Company Secretary
                                                                        Membership No.: [ ]
Place: [ ]                                     Place: [ ]
Date: [ ]                                      Date: [ ]
```
Use placeholders in square brackets where details are not provided; list them in Open Points.
For IFRS/US GAAP sets, use the local signing convention (e.g. directors' approval statement; US:
no auditor block on statements, report is separate).

## Print / PDF version
Generate a Word or PDF document (docx/pdf skills) with: cover page, index, statements, notes,
policies. Page numbers "Page X of Y", entity name in header. Tables match the workbook exactly —
generate from the workbook values after recalculation, never retype.

## Open Points tab
`# | Area | Ledger/Note | Issue | Amount | Severity | Assumption used | Action required | Owner`
Severities: Critical (blocks sign-off), High, Medium, Low.

## Final message to user
- Checks: X of Y passed; list any WARNINGs
- Key numbers: revenue, PAT, total assets, net worth, cash, net debt — both years
- Open points count by severity
- Assumptions made
- Files delivered
Short, factual, no recap of process steps.
