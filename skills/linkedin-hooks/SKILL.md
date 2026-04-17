---
name: linkedin-hooks
description: The ultimate playbook for writing LinkedIn hooks, posts, and story frameworks. Niche-agnostic by design — plug any niche in and remix. Use whenever the task is to write, review, remix, or generate a LinkedIn post, hook line, or story-shaped post. Includes a swipe-file database of real high-engagement posts tagged by pattern, a set of hook templates, full post frameworks, and generator playbooks.
---

# LinkedIn Hooks — Ultimate Skill

This skill exists to make writing **high-engagement LinkedIn posts** fast and repeatable. It is built around three tightly cross-linked layers:

1. **Hook templates** — fill-in-the-blank opening lines grouped by pattern.
2. **Story frameworks** — full-post skeletons (hook → build → payoff → CTA).
3. **Swipe database** — real posts from other creators, ranked by engagement, tagged by pattern, niche, and length, all back-linked to the hook/story templates they exemplify.

Every swipe entry links to one or more hook templates and story frameworks. Every hook template links to example swipes and the story frameworks it pairs well with. So you can enter from any direction and find what you need.

## When to use this skill

Use whenever the task involves ANY of:

- Writing a new LinkedIn post.
- Writing just the hook (first 1–3 lines) of a post.
- Rewriting / remixing a swipe in a specific niche.
- Critiquing a draft post against proven patterns.
- Generating N hook options for a given idea.
- Adapting a niche-agnostic template to a specific niche.

## How to use (fast paths)

**"I have an idea, give me hooks."**
→ Open `templates/generators/hook-generator.md`, fill in the idea + niche, get N hooks mapped to patterns.

**"I have an idea, give me a full post."**
→ Open `templates/generators/post-generator.md`, pick a story framework, fill it in.

**"I saw a post I loved, rewrite it for me."**
→ Open `templates/generators/remix-generator.md`, paste the swipe, specify your niche/angle.

**"I want to browse what works."**
→ Open `database/swipe.index.md` and filter by tag (pattern, niche, length, CTA type).

**"I want to understand why a hook works."**
→ Open `references/02-hook-taxonomy.md`, find the pattern, read the mechanics.

## Directory layout

```
skills/linkedin-hooks/
├── SKILL.md                               # You are here
├── README.md                              # Quick navigation
├── references/
│   ├── 00-overview.md                     # Mental model + vocabulary
│   ├── 01-linkedin-mechanics.md           # Feed algo, "see more" line, timing
│   ├── 02-hook-taxonomy.md                # Every hook pattern we track
│   ├── 03-story-frameworks.md             # PAS, BAB, AIDA, storytime, etc.
│   ├── 04-engagement-levers.md            # Comments, saves, reshares, DMs
│   ├── 05-voice-and-formatting.md         # Line breaks, emojis, length, readability
│   ├── 06-niche-adaptation.md             # How to remix niche-agnostic → specific
│   ├── 07-cta-and-conversion.md           # CTA types, placement, strength
│   ├── 08-anti-patterns.md                # What kills reach/trust
│   └── 99-review-checklist.md             # Ship-gate before posting
├── templates/
│   ├── hooks/                             # One file per hook pattern family
│   │   └── _base-hook.md                  # Generic pattern template
│   ├── stories/                           # Full-post frameworks
│   │   └── _base-story.md
│   └── generators/                        # Prompts / playbooks to run
│       ├── hook-generator.md
│       ├── post-generator.md
│       └── remix-generator.md
├── database/
│   ├── swipe.index.md                     # Master tagged index of all swipes
│   ├── swipe/                             # One file per swipe (raw + annotations)
│   └── entries/                           # Misc atomic knowledge (rules, quotes)
└── examples/                              # Worked niche-adaptations of swipes
```

## Intake protocol (for when you drop posts)

See `references/INTAKE.md` for the full spec. TL;DR of what happens per drop:

1. I save the raw post to `database/swipe/<NNNN>-<slug>.md` with YAML front-matter:
   - `rank`, `engagement_signal`, `creator` (if given), `length`, `hook_lines`, `cta_type`, `niche_origin`, `patterns[]`, `frameworks[]`, `tags[]`.
2. I annotate: what the hook is doing, why it works, what pattern family, what framework the body follows, what CTA.
3. I add a row to `database/swipe.index.md` (tagged + searchable).
4. If the swipe uses a **new** pattern or framework, I add it to `templates/hooks/` or `templates/stories/` and cross-link.
5. If the swipe confirms an existing pattern, I bump its swipe count and add a reference link.

You can drop posts one at a time, in batches, pasted raw, with or without creator name / engagement numbers. I'll just intake them.

## Conventions

- **Pattern slug**: lowercase, hyphenated (e.g. `curiosity-gap`, `contrarian-claim`, `stat-drop`, `before-after-bridge`, `storytime-hero-fail`).
- **Framework slug**: same style (`pas`, `bab`, `aida`, `storytime`, `listicle`, `contrarian-take`, `case-study`, `framework-drop`, `teardown`).
- **Niche tags**: freeform but reuse (`#saas`, `#ai`, `#fitness`, `#b2b`, `#career`, `#founder`, `#sales`, `#recruiting`, `#marketing`, `#finance`, ...).
- **Length tags**: `#short` (<500 chars), `#medium` (500–1200), `#long` (>1200).
- **CTA tags**: `#cta-comment`, `#cta-dm`, `#cta-save`, `#cta-share`, `#cta-none`, `#cta-follow`.

## Status legend

- `STATUS: draft` — scaffold, not yet populated from swipes.
- `STATUS: populated` — has real swipe-backed content.
- `STATUS: verified` — reviewed, cross-linked, at least 3 swipes supporting.
