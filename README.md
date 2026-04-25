# hooks-skill

The **LinkedIn Hook Writer** skill — a complete, searchable, cross-linked system for writing high-converting LinkedIn hooks.

- **`SKILL.md`** is the canonical spec (the rulebook: formats, rules, bans, workflow).
- **`EXAMPLES.md`** is the canonical reference (131 annotated hooks from 21 creators).
- Everything else here is **tooling around those two files** so they're usable end-to-end.

## What's here

```
.
├── SKILL.md                       # Canonical spec — DO NOT duplicate rules elsewhere
├── EXAMPLES.md                    # Canonical examples — parser input
├── README.md                      # You are here
│
├── database/                      # Auto-generated from EXAMPLES.md
│   ├── hooks.index.md             #   Master table (all 131 hooks, one row each)
│   ├── hooks/                     #   One file per hook, YAML front-matter + annotations
│   ├── creators/                  #   One file per creator with voice notes
│   ├── by-format/                 #   One file per format (Dense/Punchy+/Bomb/Stacked)
│   └── by-rule/                   #   One file per rule → every hook citing it
│
├── briefs/                        # Reusable hook-writing briefs (per post type)
│   ├── _base-brief.md             #   Shell all briefs extend
│   ├── data-framework-post.md
│   ├── personal-narrative-post.md
│   ├── announcement-launch-post.md
│   ├── thought-leadership-post.md
│   ├── sponsored-partnership-post.md
│   ├── case-study-post.md
│   ├── teardown-post.md
│   ├── listicle-post.md
│   ├── acknowledgment-post.md
│   └── remix-from-source.md
│
├── references/                    # Supplementary docs (do NOT duplicate SKILL.md)
│   ├── INTAKE.md                  #   How to add new hooks to the database
│   ├── niche-remix-protocol.md    #   Exact procedure for adapting hooks to a new niche
│   └── quick-lookup.md            #   "I want X → go here" cheat sheet
│
├── inbox/                         # Drop zone for unprocessed source material
│   ├── screenshots/               #   Drop new PNGs of LinkedIn hooks here
│   └── _processed/                #   PNGs land here after ingest into EXAMPLES.md
│
└── scripts/
    └── build_db.py                # Parser: EXAMPLES.md → database/
```

## How to use it

### Write hooks right now

- **From a draft**: paste it to the skill. `SKILL.md` workflow handles it.
- **From a topic**: open the brief in `briefs/` that matches the post type, fill it, send it.
- **From a source hook**: use `briefs/remix-from-source.md`.

### Learn a format or rule

- **Format**: `SKILL.md` has the rulebook. `database/by-format/<slug>.md` has every example.
- **Rule**: `database/by-rule/rule-NN.md` has every hook citing that rule.
- **Creator**: `database/creators/<slug>.md` has their hooks + pattern tendencies.

### Add new hooks to the system

See `references/INTAKE.md`. TL;DR: edit `EXAMPLES.md`, run `python3 scripts/build_db.py`.

### Adapt a hook to a different niche

See `references/niche-remix-protocol.md`.

## Conventions

- `SKILL.md` is the single source of truth for rules, formats, bans, and workflow. Other files reference it; they never re-state it.
- `EXAMPLES.md` is the single source of truth for example hooks. `database/` is derived.
- Hook ids are 4-digit, zero-padded, globally sequential across formats (0001–0131 currently).
- Rule ids are 2-digit, matching the numbering in `SKILL.md` § Hook Writing Rules.

## Stats (current)

- Hooks: **131**
- Creators: **21** (+1 placeholder)
- Formats: **4** (Dense, Punchy+Context, Single-Line Bomb, Stacked)
- Rules indexed: **14** of 40 (only rules currently cited by hooks in EXAMPLES.md)

Run `python3 scripts/build_db.py` after any edit to `EXAMPLES.md` to refresh.
