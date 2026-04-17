# Generator — Remix Generator

**Purpose**: take a swipe (either a pasted post or a swipe id from the database) and adapt it to a new niche / angle / voice while keeping what made it work.

## How to invoke

> "Use remix-generator. Swipe: <paste or 'id: NNNN'>. Niche: <target niche>. Angle: <your angle>."

Optional:

- `voice: <observational | opinionated | confessional>`
- `length: <same | shorter | longer>`
- `variants: <N>` — how many remixes (default 3)
- `preserve: <what must stay>` — e.g. "keep the stat-drop hook structure"
- `avoid: <what must not appear>` — e.g. "don't talk about funding"

## Process (what I do)

1. **Classify the swipe** — pattern(s), framework, CTA. (If it's a database swipe, I read the existing classification.)
2. **Extract the bones**:
   - Hook mechanism and shape.
   - Body beats (what each beat does, not the specific content).
   - CTA type.
3. **Swap the surface** using the niche adaptation checklist (`references/06-niche-adaptation.md`):
   - actor, stakes, metric, jargon, artifact, villain, authority.
4. **Calibrate voice register** to the target niche.
5. **Produce N variants** at different intensity / length / voice.
6. **Run the review checklist**.

## What I output

```
==== SOURCE SWIPE ====
<reference to the original — id or short quote>
- original pattern(s): <...>
- original framework: <...>
- original cta: <...>

==== REMIX: <slug of niche/angle> ====

--- Variant 1 (voice: <...>) ---
<full post>

--- Variant 2 (voice: <...>) ---
<full post>

--- Variant 3 (voice: <...>) ---
<full post>

==== WHAT STAYED, WHAT CHANGED ====
Stayed: <pattern/framework/CTA mechanics>
Changed: <actor/metric/jargon/etc>

==== CHECKLIST ====
- not a line-for-line copy: ✓
- niche-native language: ✓
- hook still self-contained: ✓
- one idea: ✓
- CTA matches goal: ✓
- flagged risks: <list or none>
```

## Rule: never line-for-line

A remix is legit when:

- **Pattern + framework + CTA type** are preserved (that's the IP of the swipe-as-lesson).
- **Surface** (nouns, verbs, numbers, stakes, jargon) is new.
- **At least one structural tweak** appears (e.g. flipped beat order, added one beat, merged two beats).

If a variant comes out too close to the source, I rewrite it.

## Good remix prompts

- "Remix swipe 0042 for `#sales` founders; angle: the mistake I made closing a 6-figure deal."
- "Paste: <post>. Niche: `#ai`. Keep the contrarian hook; swap the body to a case study."
- "Remix 0015 but confessional voice, shorter, DM CTA."

## Anti-uses

- Writing a brand-new post from scratch → `post-generator.md`.
- Brainstorming hooks only → `hook-generator.md`.

## Links

- Niche adaptation: [`../../references/06-niche-adaptation.md`](../../references/06-niche-adaptation.md)
- Swipe index: [`../../database/swipe.index.md`](../../database/swipe.index.md)
- Review checklist: [`../../references/99-review-checklist.md`](../../references/99-review-checklist.md)
