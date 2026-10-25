# How to be wrong

Each of these was a real mistake or a real near miss on a live review. The common
shape is the same: the document was defensible and the reading was not.

Read this before asserting anything.

---

## 1. Calling a rounding artefact an error

Statements are in lakhs to two decimals. A column of rounded components will
frequently not add to the rounded total. That is a presentation question, not a
misstatement.

**The test.** Go to the unrounded figure in the working paper.

- Exact sum rounds to the printed total: the components are a rounding artefact.
  The fix is to force the subtotal or absorb the difference in one line.
- Exact sum rounds to something else: it is an error.

Report which one you found, in those terms. A finding that says "the components
add to 45,576.45 against a printed subtotal of 45,576.46, and the exact sum is
45,576.4629, so the subtotal is correct and the components carry the rounding"
is useful. One that says "casting error" is not, and will be rejected.

**Choosing the plug line.** Where a rounding difference must be absorbed, put it
in the line with the largest rounding residual in the direction needed, never in
a line that is cross referenced elsewhere. Off limits: lease liabilities, which
tie to the lease note and to the consolidated; borrowings, which tie to the
classification schedule; share capital and securities premium, which tie to the
statement of changes in equity; anything appearing in the SEBI quarterly results.

---

## 2. Treating an accounting policy sentence as the disclosure

Searching the full text for "unused tax losses" hits the Ind AS 12 policy
paragraph in almost every annual report written. Searching for "disaggregation"
hits the Ind AS 115 policy. Searching for "unbilled" hits the revenue policy.
None of them is the disclosure.

Before recording a disclosure as present, confirm there is a table or a figure,
not a sentence describing the standard's requirement. Before recording one as
absent, confirm you searched for the heading as well as the keyword.

---

## 3. Assuming a change was made because the wording changed

On a repeat pass this is the main risk. The EPS numerator was corrected from
total comprehensive income to profit for the year, which was the point raised,
and the EPS figure beneath it was never recomputed. The note then asserted a
division that does not yield the number printed under it. Reading the narrative
would have recorded the point as closed.

Verify the underlying arithmetic every time, not the sentence.

---

## 4. Not noticing the notes were renumbered

Inserting one note shifts every number after it. Cross references inside the
statements and inside the auditor's report then point at the wrong note, in
bulk and silently.

This cuts both ways, and the second direction is the one that embarrasses. On a
live review six note references in the auditor's report were reported as wrong.
They were correct: the auditor had worked from the renumbered set and the
printed financial statements had used the old numbering. The correct advice was
to reject five of the six redlines previously proposed.

Before reporting a cross reference as wrong, confirm which numbering each
document was prepared against.

---

## 5. Comparing against the wrong file

These folders accumulate: `_Final Set`, `_Final Set (005)`, `_2808`, `_31082026`.
A review performed against a superseded file is worse than no review, because it
will be believed.

Inventory first. State file names and modification dates in the scope note.
Where two files have identical sizes and timestamps, say so rather than picking.

---

## 6. Writing into the client's workbook with a library

`openpyxl` reads these files correctly and destroys them on save. A round trip
test on a live 3 MB working set lost 86 internal relationship parts: pivot
links, hyperlinks, sheet relations. The file still opens, so the damage is not
obvious until someone needs the pivots.

Test it before writing anything:

```python
import zipfile
before = set(zipfile.ZipFile(src).namelist())
# load and save with the library
after = set(zipfile.ZipFile(out).namelist())
print(len(before - after), "parts lost")
```

Where it loses parts, drive Excel itself through COM, or deliver the additions
as a separate workbook for the team to copy across. Say which you did and why.
See the `review-markup` skill.

---

## 7. Reading text extraction as if it were the page

`pdftotext -layout` approximates columns with spaces. On a tight financial table
the approximation collapses and figures land under the wrong heading, silently.
Use the layout preserving extractor in `scripts/extract.py`, and render the page
to an image whenever a digit matters or a figure looks implausible.

Extraction also drops and inserts punctuation. A comma reported as missing from
an opinion paragraph turned out to be present on the page and absent only from
the extraction. Check the rendered page before reporting a punctuation finding.

---

## 8. Over reading a blank cell

A blank comparative column may be a missing figure, or it may be a line that did
not exist in the prior year. A nil in a prior year column may be a genuine nil
or an unpopulated cell. Both are worth raising, but as different findings and in
different registers.

Where the prior year published annual report is available, check what was
actually reported last year before calling a comparative wrong.

---

## 9. Treating the Excel as authoritative

It usually is, but not always. Where the printed statement and the working paper
disagree, establish which is right rather than assuming the Excel wins. On a
live review the Excel balance sheet subtotals were each about 0.01 above the sum
of the lines beneath them, because a SUM range was over reaching across a
duplicated row label. The print was right and the working paper was wrong.

Re foot the Excel too.

---

## 10. Asserting a legal conclusion from a checklist

Section 135 applicability turns on the immediately preceding financial year, not
on a three year average. Section 186(11) exempts a wholly owned subsidiary
company, which does not cover a limited liability partnership. Minimum promoters'
contribution is locked in for eighteen months and the balance for six, and which
shares sit in which block decides whether an encumbrance is permitted.

Where a finding depends on a provision, read the provision. Where it depends on
facts outside the documents, such as which shares form the minimum promoters'
contribution, raise it as a question for the company secretary and a securities
lawyer rather than as a conclusion. Flag it as requiring confirmation, in terms,
and say what would settle it.

---

## 11. Burying the finding that matters

A review producing sixty observations, of which four stop publication, must open
with the four. The reader's attention is finite and spends itself in the first
page. Rank by consequence to the reader, not by the order the documents happened
to raise them.
