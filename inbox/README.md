# Inbox

Drop zone for unprocessed source material — primarily PNG screenshots of LinkedIn posts to ingest into the database.

## Folder layout

```
inbox/
├── README.md           # You are here
├── screenshots/        # Drop new PNGs here
└── _processed/         # I move PNGs here after they've been ingested into EXAMPLES.md
```

## How to drop

1. Put PNG files into `inbox/screenshots/`.
2. Filenames don't have to be perfect. Any of these are fine:
   - `IMG_0421.png`
   - `screenshot-2026-04-25.png`
   - `jake-ward-seo.png`
   - `001.png`
3. Optional but helpful: prefix with a number for ordering, or include the creator name if you remember it.
4. Commit and push.

## How I'll process them

For each PNG in `inbox/screenshots/`:

1. **Read the image** — extract the hook text verbatim (line breaks preserved), creator name (if visible), and any visible engagement signal (likes, comments, reposts, impressions).
2. **Classify the format** against [`../SKILL.md`](../SKILL.md) — Dense / Punchy+Context / Single-Line Bomb / Stacked.
3. **Identify the rules** the hook exercises (cite by rule number from `SKILL.md`).
4. **Append a properly-formatted block** to [`../EXAMPLES.md`](../EXAMPLES.md) under the right format + creator section, following the exact shape in [`../references/INTAKE.md`](../references/INTAKE.md).
5. **Re-run the parser** — `python3 scripts/build_db.py` — to regenerate `database/`.
6. **Move the PNG** to `inbox/_processed/` so I don't double-ingest it.
7. **Commit** with a message like `Ingest N hooks from inbox (creators: X, Y, Z)`.

## Per-batch summary

After each batch I process, I'll add a one-line summary in this README under "Processing log" (below) so we have a paper trail.

## Conventions per ingest

- **Verbatim text.** No paraphrasing. Capitalization, punctuation, line breaks, ellipses preserved exactly as in the screenshot.
- **Width / lines on mobile.** I'll estimate from the screenshot if visible; otherwise compute from char count using the heuristics in `SKILL.md` § LinkedIn Mechanics.
- **Unknown creator.** If the creator isn't identifiable from the screenshot, I file the hook under `### Unknown` within the matching format section, and flag in the commit message so you can backfill if you remember.
- **Duplicates.** Before adding, I search EXAMPLES.md for the first 60 chars of the hook. If it already exists, I skip and note in the commit message.
- **Multi-hook screenshots.** If one PNG contains multiple distinct hook examples (e.g. a teardown carousel screenshot), I split into one EXAMPLES.md entry per hook.
- **Non-hook content.** If a PNG is a note/framework/tip rather than a real LinkedIn post hook, I file it in `references/captured-notes.md` (created on first occurrence) instead of EXAMPLES.md.

## Anti-patterns (don't)

- Don't put PNGs anywhere except `inbox/screenshots/`.
- Don't manually edit `database/` — it's regenerated.
- Don't manually move PNGs to `_processed/` — that's my signal that I've ingested them.

## Processing log

_(I append one entry per batch.)_

- _none yet — waiting for first drop_
