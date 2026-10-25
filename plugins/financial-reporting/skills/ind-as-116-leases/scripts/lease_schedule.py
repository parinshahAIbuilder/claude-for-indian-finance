#!/usr/bin/env python3
"""Ind AS 116 lessee schedule with an IGAAP (straight-line rent) comparison.

Example:
  python lease_schedule.py --rent 250000 --months 108 --ibr 10.5 \
      --escalation 15 --escalation-every 36 --rent-free 2 --out lease1

Payments are assumed monthly in advance unless --arrears is given.
Writes <out>_indas.csv and <out>_bridge.csv and prints a summary.
"""
import argparse
import csv


def payments(rent, months, escalation, every, rent_free):
    out = []
    current = rent
    for m in range(months):
        if every and m > 0 and m % every == 0:
            current = current * (1 + escalation / 100)
        out.append(0.0 if m < rent_free else round(current, 2))
    return out


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--rent", type=float, required=True, help="monthly rent at commencement (excl. GST)")
    ap.add_argument("--months", type=int, required=True, help="lease term in months")
    ap.add_argument("--ibr", type=float, required=True, help="annual incremental borrowing rate, %")
    ap.add_argument("--escalation", type=float, default=0.0, help="escalation %, applied every N months")
    ap.add_argument("--escalation-every", type=int, default=0, help="N months between escalations")
    ap.add_argument("--rent-free", type=int, default=0, help="rent-free months at the start")
    ap.add_argument("--idc", type=float, default=0.0, help="initial direct costs and other ROU additions")
    ap.add_argument("--arrears", action="store_true", help="payments at end of each month")
    ap.add_argument("--out", default="lease")
    a = ap.parse_args()

    r = (1 + a.ibr / 100) ** (1 / 12) - 1  # effective monthly rate
    pay = payments(a.rent, a.months, a.escalation, a.escalation_every, a.rent_free)

    if a.arrears:
        liability = sum(p / (1 + r) ** (i + 1) for i, p in enumerate(pay))
    else:
        liability = sum(p / (1 + r) ** i for i, p in enumerate(pay))
    rou = liability + a.idc
    dep = rou / a.months
    sl_rent = sum(pay) / a.months  # AS 19 straight-line

    rows, bridge = [], []
    bal = liability
    for i, p in enumerate(pay):
        opening = bal
        if a.arrears:
            interest = opening * r
            bal = opening + interest - p
        else:
            after_pay = opening - p
            interest = after_pay * r
            bal = after_pay + interest
        rows.append([i + 1, round(opening, 2), p, round(interest, 2), round(bal, 2), round(dep, 2)])
        indas_cost = interest + dep
        bridge.append([i + 1, round(indas_cost, 2), round(sl_rent, 2), round(sl_rent - indas_cost, 2)])

    with open(f"{a.out}_indas.csv", "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["month", "opening_liability", "payment", "interest", "closing_liability", "rou_depreciation"])
        w.writerows(rows)
    with open(f"{a.out}_bridge.csv", "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["month", "indas_pl_charge", "igaap_straight_line_rent", "pat_difference_igaap_minus_indas"])
        w.writerows(bridge)

    yr1_indas = sum(b[1] for b in bridge[:12])
    yr1_igaap = sum(b[2] for b in bridge[:12])
    print(f"Initial lease liability : {liability:,.2f}")
    print(f"Initial ROU asset       : {rou:,.2f}")
    print(f"Monthly ROU depreciation: {dep:,.2f}")
    print(f"Total undiscounted rent : {sum(pay):,.2f}")
    print(f"Year 1 P&L charge  Ind AS: {yr1_indas:,.2f}  IGAAP: {yr1_igaap:,.2f}  difference: {yr1_indas - yr1_igaap:,.2f}")
    print(f"Closing liability check : {bal:,.2f} (should be ~0)")


if __name__ == "__main__":
    main()
