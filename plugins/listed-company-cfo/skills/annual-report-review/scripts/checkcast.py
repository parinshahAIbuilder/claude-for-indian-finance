#!/usr/bin/env python
"""Re foot a block and say whether a difference is an error or a rounding artefact.

    python checkcast.py --total 45576.46 6454.28 6978.37 19225.26 333.64 29.63 \
                        4863.04 26.21 3969.02 849.60 2847.41

    python checkcast.py --total 51771.52 --exact 13059.2753 5456.5943 33255.6507

Rounds half up to two decimals, which is the convention these statements use.
Python's round() is banker's rounding and will disagree on a .005 boundary, so
do not use it for this.

Pass --exact values (the unrounded working paper figures) to settle the question
that decides the finding:

  exact sum rounds to the printed total   -> rounding artefact, force the subtotal
  exact sum rounds to something else      -> error

Where a rounding difference must be absorbed, put it in the line with the largest
residual in the direction needed, and never in a line that is cross referenced
elsewhere. Off limits: lease liabilities, borrowings, share capital, securities
premium, anything in the SEBI quarterly results.
"""
import argparse, sys
from decimal import Decimal, ROUND_HALF_UP

sys.stdout.reconfigure(encoding="utf-8", errors="replace")


def R(x):
    return Decimal(str(x)).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("values", nargs="+", type=str)
    ap.add_argument("--total", type=str, required=True)
    ap.add_argument("--exact", action="store_true",
                    help="values are unrounded working paper figures")
    ap.add_argument("--labels", help="comma separated labels, same order as values")
    a = ap.parse_args()

    vals = [Decimal(v.replace(",", "")) for v in a.values]
    total = Decimal(a.total.replace(",", ""))
    labels = (a.labels.split(",") if a.labels else [""] * len(vals))
    labels += [""] * (len(vals) - len(labels))

    exact = sum(vals)
    rounded_sum = sum(R(v) for v in vals)
    exact_rounded = R(exact)

    w = max([len(l) for l in labels] + [10])
    print(f"{'line':<{w}}  {'value':>16}  {'rounds to':>12}  {'residual':>10}")
    print("-" * (w + 44))
    for lab, v in zip(labels, vals):
        print(f"{lab.strip():<{w}}  {v:>16}  {R(v):>12}  {R(v)-v:>10}")
    print("-" * (w + 44))
    print(f"{'exact sum':<{w}}  {exact:>16}  {exact_rounded:>12}")
    print(f"{'sum of rounded':<{w}}  {'':>16}  {rounded_sum:>12}")
    print(f"{'printed total':<{w}}  {'':>16}  {total:>12}")
    print()

    if a.exact:
        if exact_rounded == total:
            d = total - rounded_sum
            if d == 0:
                print("CLEAN. Exact sum rounds to the printed total and the rounded")
                print("components add to it. No exception.")
            else:
                print(f"ROUNDING ARTEFACT. The printed total is CORRECT: the exact sum")
                print(f"{exact} rounds to {total}. The rounded components add to")
                print(f"{rounded_sum}, a difference of {d}, because individual roundings")
                print("accumulate.")
                print()
                print("Report it as a presentation point, not an error. Fix by forcing")
                print("the subtotal, or absorb the difference in the line with the")
                print("largest residual in the direction needed:")
                order = sorted(zip(labels, vals), key=lambda t: (R(t[1]) - t[1]) * (1 if d > 0 else -1))
                for lab, v in order[:3]:
                    print(f"      {lab.strip() or str(v):<{w}}  residual {R(v)-v}")
        else:
            print(f"ERROR. The exact sum {exact} rounds to {exact_rounded},")
            print(f"not to the printed {total}. Difference {exact_rounded - total}.")
    else:
        d = total - rounded_sum
        if d == 0:
            print("Components add to the printed total. No exception.")
        else:
            print(f"DOES NOT FOOT by {d}.")
            print()
            print("Before reporting this, get the unrounded figures from the working")
            print("paper and run again with --exact. A column of rounded components")
            print("frequently will not add to a correctly rounded total, and that is")
            print("a presentation point rather than a misstatement.")


if __name__ == "__main__":
    main()
