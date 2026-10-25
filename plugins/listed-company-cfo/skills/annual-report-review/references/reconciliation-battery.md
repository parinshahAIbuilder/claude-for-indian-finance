# The reconciliation battery

Work through this rather than improvising. Every test is arithmetic and either
agrees or does not. Run each for both years.

Record the result of every test, including the ones that pass.

---

## A. Balance sheet

1. Non current assets: components sum to the stated subtotal.
2. Current assets: components sum to the stated subtotal.
3. Total assets equals the two subtotals.
4. Equity: share capital plus other equity equals total equity.
5. Non current liabilities: components sum to the subtotal.
6. Current liabilities: components sum to the subtotal.
7. Total equity and liabilities equals the three subtotals.
8. **Total assets equals total equity and liabilities.** Both years.

Where 8 fails, the cause is almost always one subtotal, not the total. Find
which block does not foot before proposing a fix.

Then:

9. Every balance sheet line agrees to its note total.
10. Current versus non current split is consistent with the note.
11. Note references on the face point at the right note.
12. Comparative column agrees to the prior year published annual report.

---

## B. Statement of profit and loss

1. Revenue plus other income equals total income.
2. The expense lines sum to total expenses.
3. Total income less total expenses equals profit before exceptional items and tax.
4. That figure adjusted for exceptional items equals profit before tax, **and the
   caption matches the arithmetic**. An exceptional income shown in brackets
   under a caption reading "(V minus VI)" reaches the right answer only because
   a negative is being subtracted. Flag it.
5. Current tax plus deferred tax plus earlier year adjustments equals total tax.
6. Profit before tax less total tax equals profit for the year.
7. Other comprehensive income components sum to the OCI total.
8. Profit plus OCI equals total comprehensive income.
9. Both OCI categories are presented, items that will and will not be
   reclassified, with nil against the one that is empty. Ind AS 1 paragraph 82A.
10. Every expense line agrees to its note.
11. Roman numeral sequence on the face is unbroken.

---

## C. Earnings per share

The single most error prone note in the set. Test all of it.

1. **The numerator is profit attributable to equity holders, not total
   comprehensive income.** Ind AS 33 paragraph 9. Where the two differ, confirm
   which was used by dividing.
2. Preference dividend is deducted where preference shares are outstanding, in
   both years, consistently.
3. Numerator less preference dividend equals the stated net profit attributable
   to equity shareholders.
4. **Numerator divided by weighted average shares equals the printed EPS.** Do
   the division. This is where corrected numerators meet uncorrected EPS lines.
5. Weighted average shares are consistent with the share movement in note on
   share capital and with the dates of issue.
6. Bonus issues and splits are applied retrospectively to all periods presented.
7. Diluted equals basic only where there are no dilutive potential equity
   shares, and that is stated.
8. The numerator agrees to the face of the profit and loss, to the paisa.
9. Standalone and consolidated use the same basis.

---

## D. Statement of changes in equity

1. Share capital table closes at the figure on the face of the balance sheet.
   Where preference capital sits inside equity share capital on the face and is
   absent here, the gap is unexplained and the reader cannot reconcile.
2. Each column foots down.
3. **Each row cross casts across**: retained earnings plus reserves equals total.
4. Closing total equals other equity on the balance sheet.
5. Closing total equals the closing figure in the other equity note.
6. Profit for the year agrees to the profit and loss.
7. OCI for the year agrees to the profit and loss.
8. There is no row that both appears as a movement and duplicates the sum of
   other movements. A "total comprehensive income" row sitting alongside separate
   profit and OCI rows double counts.
9. Restated balance at the beginning of the period is present where required.
10. Consolidated carries a separate non controlling interest column, and the NCI
    movement reconciles to the balance sheet and the profit allocation.

---

## E. Cash flow statement

1. Operating adjustments sum to operating profit before working capital changes.
2. Working capital movements sum to the stated net change.
3. Cash generated from operations plus taxes equals net cash from operations.
4. Investing components sum to the investing total.
5. Financing components sum to the financing total.
6. The three totals sum to the net movement.
7. Opening cash plus net movement equals closing cash.
8. **Closing cash equals the balance sheet and the cash and cash equivalents note.**
9. Depreciation added back equals the depreciation note and the fixed asset
   schedule.
10. Finance cost added back reconciles to the finance cost note, with any
    difference explained.
11. Interest paid reconciles to finance cost and the movement in interest accrued.
12. Lease payments reconcile to the lease liability roll forward. Interest plus
    principal paid must equal the payment line in the lease note.
13. Movements in bank deposits that are not cash equivalents appear as a separate
    investing line. A balance going from nil to a material figure with no line in
    investing is a presentation failure under Ind AS 7.
14. The Ind AS 7 paragraph 44A reconciliation of liabilities arising from
    financing activities is present and foots to the opening and closing
    borrowings and lease liabilities.

---

## F. Notes, both directions

**Face to note.** Every figure on the face is supported by a note.

**Note to face.** Every note total flows correctly to the face.

Within each note:

1. Components sum to the stated total, both years.
2. Matrix schedules foot across and down, and the grand total equals both. Fixed
   asset and intangible schedules, receivable and payable ageing.
3. Opening plus movements equals closing in every roll forward.
4. Deductions are presented with the sign the formula uses. A deduction printed
   as a positive that the total subtracts is wrong on the page even though the
   total is right.
5. Ageing analyses: the net figure after expected credit loss equals the balance
   sheet.
6. Related party transaction and balance tables agree to the loans, borrowings
   and trade receivable notes.
7. Contingent liability narrative figures agree to the contingent liability table
   and to the CARO statutory dues table.
8. Fair value tables include every financial asset and liability on the balance
   sheet, and the carrying values agree.
9. Maturity analyses described as undiscounted actually are undiscounted.
10. Any note total used in a ratio agrees to the ratio working.

---

## G. Standalone against consolidated

Same figure, same policy, same words, unless consolidation explains the
difference.

1. Securities premium. A holding company balance. It cannot differ.
2. Equity share capital and the share movement.
3. EPS basis and methodology.
4. Lease liabilities and lease cash flows, where the subsidiaries hold no leases.
5. Accounting policy wording.
6. Note numbering, and therefore every cross reference.
7. The description given to the same equity adjustment.
8. Spelling corrections applied to one set and not the other.
9. Contingent liabilities, with eliminations explained.
10. Where consolidated is lower than standalone for an additive item, there is an
    error. Consolidation adds.

---

## H. Working paper tie out

1. Every printed note total exists in the Excel and agrees.
2. The current year columns in the Excel are populated. Empty current year
   columns against fully populated prior year columns means the file is last
   year's.
3. Formula errors: `#REF!`, `#VALUE!`, `#DIV/0!` anywhere in a sheet feeding a
   printed figure.
4. Open preparer notes left in cells: "to be confirmed", "pending", "not done",
   "to be discussed", "check".
5. Hardcoded figures where a formula is expected, particularly in subtotals.
6. Subtotal formulas whose range over reaches or under reaches, usually caused by
   a duplicated or blank row label.
7. Tax computation resolves to a number and that number agrees to the current tax
   charge in the profit and loss. Where it does not, establish whether the
   difference is minimum alternate tax, and if so whether MAT credit has been
   recognised.
8. Deferred tax working closes at the balance sheet figure, and the movement
   equals the profit and loss charge plus the OCI charge.
