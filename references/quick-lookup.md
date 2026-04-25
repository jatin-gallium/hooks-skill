# Quick Lookup

Fast "I want X → go here" map across SKILL.md, EXAMPLES.md, database, and briefs.

## I want to…

### Write hooks right now

- From a **draft post** → paste it + invoke [`../SKILL.md`](../SKILL.md) directly. The skill handles it.
- From a **topic only** → pick the matching brief in [`../briefs/`](../briefs/), fill it, send it.
- From a **source hook** I liked → [`../briefs/remix-from-source.md`](../briefs/remix-from-source.md).

### Learn a format

- Dense: [`../SKILL.md`](../SKILL.md) § Format 1 + [`../database/by-format/dense.md`](../database/by-format/dense.md).
- Punchy+Context: [`../SKILL.md`](../SKILL.md) § Format 2 + [`../database/by-format/punchy-context.md`](../database/by-format/punchy-context.md).
- Single-Line Bomb: [`../SKILL.md`](../SKILL.md) § Format 3 + [`../database/by-format/single-line-bomb.md`](../database/by-format/single-line-bomb.md).
- Stacked: [`../SKILL.md`](../SKILL.md) § Format 4 + [`../database/by-format/stacked.md`](../database/by-format/stacked.md).

### Find every hook that uses Rule N

- [`../database/by-rule/`](../database/by-rule/) — one file per rule with every hook citing it.

### Find every hook by a specific creator

- [`../database/creators/`](../database/creators/) — one file per creator with all their hooks + voice notes.

### See all hooks in one table

- [`../database/hooks.index.md`](../database/hooks.index.md).

### See the raw source

- [`../EXAMPLES.md`](../EXAMPLES.md) — canonical; hand-authored; parser input.

### Add new hooks to the database

- [`./INTAKE.md`](./INTAKE.md).

### Adapt a hook to a new niche

- [`./niche-remix-protocol.md`](./niche-remix-protocol.md).

## Cheat-sheet: which brief for which post?

| Post I'm writing                                    | Brief                                                                    |
| --------------------------------------------------- | ------------------------------------------------------------------------ |
| I have a number / stat / framework                  | [`../briefs/data-framework-post.md`](../briefs/data-framework-post.md)   |
| Founder story / career pivot / belief changed       | [`../briefs/personal-narrative-post.md`](../briefs/personal-narrative-post.md) |
| New product / feature / event launch                | [`../briefs/announcement-launch-post.md`](../briefs/announcement-launch-post.md) |
| Hot take / opinion / industry prediction            | [`../briefs/thought-leadership-post.md`](../briefs/thought-leadership-post.md) |
| Paid / sponsored / partnership                      | [`../briefs/sponsored-partnership-post.md`](../briefs/sponsored-partnership-post.md) |
| Client win / case study / receipts                  | [`../briefs/case-study-post.md`](../briefs/case-study-post.md)           |
| Analyzing someone else's post/ad/launch             | [`../briefs/teardown-post.md`](../briefs/teardown-post.md)               |
| List post (N tips / N mistakes / wins+losses)       | [`../briefs/listicle-post.md`](../briefs/listicle-post.md)               |
| Shout-out / acknowledgment / gratitude              | [`../briefs/acknowledgment-post.md`](../briefs/acknowledgment-post.md)   |
| Remix a hook I saw                                  | [`../briefs/remix-from-source.md`](../briefs/remix-from-source.md)       |

## Which format for which post?

(Heuristics — not hard rules. See [`../SKILL.md`](../SKILL.md) § Media and Hook Strategy.)

| Situation                                 | Format bias                                          |
| ----------------------------------------- | ---------------------------------------------------- |
| Text-only post, needs context             | Dense                                                |
| Text-only post, claim is sharp            | Single-Line Bomb or Punchy+Context                   |
| Strong image attached                     | Short Punchy+Context or Single-Line Bomb             |
| Chart / graph / data viz attached         | Stacked sub-variant C (Data-Question Opener)         |
| Video attached                            | Single-Line Bomb or short Punchy+Context             |
| Carousel (list content)                   | Dense list-promise OR Punchy+Context                 |
| Contrarian opinion                        | Single-Line Bomb or Punchy+Context with "Hot Take:"  |
| Before/after transformation               | Stacked sub-variant A (Before/After Timeline)        |
| Parallel regrets / patterns of behavior   | Stacked sub-variant B (Parallel Regret Stack)        |
| Expert-audience jargon play               | Stacked sub-variant D (Stacked Jargon Repetition)    |
| Product/feature post with a 3-beat arc    | Stacked sub-variant E (Problem-Cost-Twist)           |

## Keyboard-friendly search patterns

(Run from repo root.)

- Hooks citing Rule 2 → `rg -l "rules: \[.*\b2\b" database/hooks/`
- Hooks by a creator → `rg -l "creator_slug: jake-ward" database/hooks/`
- All Dense hooks → `rg -l "format_slug: dense" database/hooks/`
- Phrase search across raw hooks → `rg "SEO has been dying" database/hooks/`
