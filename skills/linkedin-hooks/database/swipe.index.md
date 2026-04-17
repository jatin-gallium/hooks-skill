# Swipe Index

The master tagged index of every swipe in `database/swipe/`. Add a row per ingest; never delete rows (mark as `deprecated` if needed).

## How to use

- **Scan by eye** — the table is sorted by `id`.
- **Filter by tag** — `rg "#tag" swipe.index.md`.
- **Filter by pattern** — grep the `patterns` column.
- **Filter by niche** — grep the `niche_origin` column.

## Columns

| id | creator | engagement | niche_origin | length | patterns | framework | cta_type | tags | file |
|----|---------|------------|--------------|--------|----------|-----------|----------|------|------|
<!-- swipes appended below this line -->

## Counts

- **Total swipes**: 0
- **By pattern (dominant)**: _to be populated_
- **By framework**: _to be populated_
- **By niche_origin**: _to be populated_
- **By length**: _to be populated_
- **By cta_type**: _to be populated_

_This section is regenerated on every ingest batch._

## Emerging observations

_Every ~50 swipes ingested, I append notes here about patterns that are emerging:_

- (none yet)
