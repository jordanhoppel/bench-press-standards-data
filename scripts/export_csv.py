#!/usr/bin/env python3
"""Turn data/bench_standards.json into the three CSV files in data/.

  python3 -I scripts/export_csv.py
"""
import csv, json, os

here = os.path.dirname(os.path.abspath(__file__))
data_dir = os.path.join(here, "..", "data")
d = json.load(open(os.path.join(data_dir, "bench_standards.json")))

def write(name, fields, rows):
    with open(os.path.join(data_dir, name), "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        w.writerows(rows)

wc = ["sex", "class_kg", "n"] + [f"p{q}_{u}" for u in ("kg", "lb") for q in (10, 25, 50, 75, 90)]
write("weight_class_percentiles.csv", wc, d["weight_classes"])
ratio = ["sex", "n", "p10", "p25", "p50", "p75", "p90"]
write("bodyweight_ratio_percentiles.csv", ratio, d["bodyweight_ratio"])
write("age_ratio_percentiles.csv", ["sex", "age"] + ratio[1:], d["by_age_ratio"])
print("wrote 3 CSV files")
