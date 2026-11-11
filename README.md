# Raw bench press percentiles from OpenPowerlifting

Percentile tables for the bench press, built from the public OpenPowerlifting database. The tables cover adults who entered raw full-power meets from 2015-01-01 to 2026-11-01, using the 2026-11-07 release.

These numbers describe people who competed. They are not percentiles of the general gym-going population, who are on average weaker.

Readable version with the tables: https://modernmensfitness.com/bench-press-standards/

## Files

| File | What it holds |
|---|---|
| `data/weight_class_percentiles.csv` | Best bench in kg and lb at the 10th, 25th, 50th, 75th and 90th percentile, by sex and IPF weight class |
| `data/bodyweight_ratio_percentiles.csv` | Bench divided by bodyweight, by sex |
| `data/age_ratio_percentiles.csv` | Bench divided by bodyweight, by sex and age group |
| `data/bench_standards.json` | The same tables plus the filters, counts and source file name |
| `scripts/build_bench_standards.py` | Rebuilds the JSON from the OpenPowerlifting CSV |
| `scripts/export_csv.py` | Writes the three CSV files from the JSON |

## Method

- Equipment is Raw and event is SBD (full power). Meet date 2015-01-01 or later. Sex is M or F.
- Place is a number or G (guest). Disqualified, doping-flagged and no-show entries are dropped.
- Best3BenchKg above 0 and a recorded bodyweight.
- Adults only: Age of 18 or more, or, when Age is blank, an age class or birth-year class that starts at 18 or more.
- One value per lifter: the best successful bench across all qualifying meets, placed in the current IPF weight class for the bodyweight at that meet.
- People are matched by name, so two lifters who share a name are merged. This slightly understates counts. It does not inflate any value.
- Age table: needs a numeric Age. Each lifter counts once per age group they competed in, using their best bench-to-bodyweight ratio in that group.
- Any cell with fewer than 200 lifters is dropped.

Counts for this release: 199,726 men and 99,528 women (distinct names), from 842,890 qualifying entries. The full drop counts are in `data/bench_standards.json`.

## Limits

- Lifters who enter meets are self-selected and stronger than the average lifter.
- A lifter's best bench across meets can come from a different bodyweight or age than the one in the table row they are placed in. Weight class is set by the bodyweight at the meet of the best bench.
- Name matching is imperfect in both directions.
- Raw here means bare knees or knee sleeves, with no bench shirt, as OpenPowerlifting defines it.

## Rebuild

1. Download the OpenPowerlifting CSV from https://openpowerlifting.gitlab.io/opl-csv/files/openpowerlifting-latest.zip and unzip it into its own folder.
2. Run `python3 -I scripts/build_bench_standards.py path/to/openpowerlifting-YYYY-MM-DD-*.csv` (needs numpy).
3. Run `python3 -I scripts/export_csv.py`.

## Source and licence

Source data: OpenPowerlifting, https://www.openpowerlifting.org, released into the public domain.

The tables and scripts in this repository are released under CC0 1.0. You can copy and reuse them without asking. A link back is welcome and not required.

## Cite

See `CITATION.cff`, or: Hoppel, J. (2026). Raw bench press percentiles from OpenPowerlifting full-power meets, 2015 to 2026 [Data set]. https://modernmensfitness.com/bench-press-standards/
