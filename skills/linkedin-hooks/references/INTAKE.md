# INTAKE — How Swipe Drops Are Processed

This is the contract for how you (the user) feed posts into the database, and what I do with them.

## How to drop posts

**Minimum**: paste the raw post text. That's literally enough.

**Better**: add any of these (freeform, in any order, before or after the post):

- `creator: <name>` — who wrote it.
- `engagement: <signal>` — e.g. `5k likes`, `top 1%`, `2M views`, `high comments`.
- `rank: <n>` — if you're dropping a ranked list, the rank within it.
- `niche: <tag>` — the niche the post lives in (you'll still use remix to adapt later).
- `source: <url>` — permalink if you have it.
- `notes: <anything>` — your own observations.

**Bulk drops**: separate posts with a line of three dashes: `---` on its own line.

**Examples of valid drops:**

```
<post text>
```

```
creator: Alex Hormozi
engagement: 12k likes
niche: founder

<post text>
```

```
rank: 1
engagement: top 1%

<post 1>
---
rank: 2
engagement: top 1%

<post 2>
---
rank: 3

<post 3>
```

I'll accept whatever you give me and fill in the rest by inference.

## What I do with each drop

For every post I ingest, I:

1. **Create** `database/swipe/<NNNN>-<slug>.md` where:
   - `<NNNN>` is zero-padded sequential id (`0001`, `0002`, ...).
   - `<slug>` is a short kebab-case summary of the hook (e.g. `stat-drop-47312-ad-spend`).

2. **Add YAML front-matter** with:
   ```yaml
   ---
   id: 0001
   creator: <name or "unknown">
   rank: <n or null>
   engagement: <string or null>
   niche_origin: <tag or "unknown">
   length: short | medium | long | max-long
   length_chars: <int>
   hook_lines: <int>           # number of lines before the visual "see more" cutoff
   patterns: [pattern-slug-1, pattern-slug-2?]  # dominant first
   framework: <framework-slug>
   cta_type: <cta-slug>
   tags: [#tag1, #tag2, ...]
   source: <url or null>
   ingested_at: <YYYY-MM-DD>
   ---
   ```

3. **Store the raw post verbatim** in a ```` ```raw ```` code block so it's preserved exactly.

4. **Annotate** with sections:
   - **Hook mechanics** — what the first line does, which pattern, why it works.
   - **Body structure** — beat-by-beat walk-through, which framework.
   - **CTA** — type + quality.
   - **Why it works** — 2–4 bullet points.
   - **Remix notes** — what's niche-specific, what's portable, what to swap for different niches.

5. **Update** `database/swipe.index.md` — add a row with tags so the swipe is findable.

6. **Cross-link**:
   - From each pattern's template in `templates/hooks/<pattern>.md` — bump the swipe count + add the link.
   - From the framework's template in `templates/stories/<framework>.md` — same.
   - If this swipe reveals a **new** pattern or framework not yet in the taxonomy, I create the template and update `references/02-hook-taxonomy.md` or `03-story-frameworks.md`.

## Swipe file template (what each `database/swipe/NNNN-*.md` looks like)

See `database/_swipe-entry.template.md` — I use that template as the shell for every swipe.

## Search / retrieval

To find swipes later:

- **By pattern**: `rg -l "patterns:.*\bcuriosity-gap\b" database/swipe/`
- **By framework**: `rg -l "framework:.*\bstorytime\b" database/swipe/`
- **By niche**: `rg -l "niche_origin:.*\bsaas\b" database/swipe/`
- **By length**: `rg -l "length: short" database/swipe/`
- **By tag**: `rg "#cta-dm" database/swipe.index.md`
- **Full-text**: `rg "<phrase>" database/swipe/`

Or just open `database/swipe.index.md` and scan.

## What to expect from me per drop

- If you drop 1 post → full processing (file + index + cross-links) in one go.
- If you drop 5–20 posts → same, but I'll batch the index updates at the end.
- If you drop 50+ posts at once → I'll process in chunks, commit periodically, and checkpoint progress so nothing is lost.
- I'll pattern-mine every ~50 posts to surface: **emerging pattern families**, **recurring framework+pattern pairings**, **niche-specific tics**.

## What I do NOT do

- I don't paraphrase the raw post. Raw text is preserved verbatim.
- I don't guess at `creator` if you didn't say.
- I don't ingest duplicates — if a post looks identical to an existing swipe, I link to the existing one instead of creating a new file.
