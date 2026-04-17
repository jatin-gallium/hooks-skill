# Generator — Post Generator

**Purpose**: given an idea (and optionally a chosen hook), produce a full LinkedIn post using a named story framework.

## How to invoke

> "Use post-generator. Idea: <idea>. Niche: <niche>. Framework: <framework or 'suggest'>. Goal: <reach | list | DMs | saves | shares>."

Optional:

- `hook: <specific hook text>` — use this exact hook.
- `hook-pattern: <pattern-slug>` — let me write the hook using this pattern.
- `voice: <observational | opinionated | confessional>`
- `length: <short | medium | long>`
- `cta: <cta-slug | suggest | none>`
- `constraints: <e.g. "no emojis", "no numbers I haven't verified">`

If I don't have a hook and no pattern, I'll generate 3 hook candidates first, let you pick, then write the post.

## Process (what I do)

1. **Pick or confirm the framework** — from `references/03-story-frameworks.md`. If you said `suggest`, I match framework to idea type (see decision table in that doc).
2. **Pick or confirm the hook pattern** — the hook must set up the framework.
3. **Draft the post** following the framework's beat-by-beat skeleton (see `templates/stories/<framework>.md`).
4. **Apply voice & formatting rules** from `references/05-voice-and-formatting.md`.
5. **Add a single CTA** matched to the goal (`references/07-cta-and-conversion.md`).
6. **Run the review checklist** (`references/99-review-checklist.md`) and flag anything that fails.

## What I output

Three blocks:

```
==== POST ====
<the post, ready to paste>

==== ANNOTATIONS ====
- hook pattern: <slug>
- framework: <slug>
- cta: <slug>
- length: <chars> (<band>)
- hook chars: <n>  ("see more" safe: yes/no)
- voice: <...>

==== CHECKLIST ====
- hook self-contained: ✓/✗
- one idea: ✓/✗
- body pays off hook: ✓/✗
- concrete specifics: ✓/✗
- single CTA: ✓/✗
- mobile-previewed shape: ✓/✗
- not a straight copy of a swipe: ✓/✗
- flagged risks: <list or none>

==== VARIANTS (optional, on request) ====
- shorter version: <...>
- more opinionated: <...>
- more confessional: <...>
```

## Niche adaptation

Baked in. If you say `niche: <tag>`, every `[ACTOR]`, `[METRIC]`, `[STAKES]`, `[VILLAIN]`, `[ARTIFACT]` gets filled with niche-native choices. Numbers are marked `[illustrative]` if speculative so you don't post unverified claims.

## Asking for iterations

Good iteration prompts:

- "Make the hook sharper, keep the body."
- "Body is too long — cut 30%."
- "Swap the framework to `<other>`."
- "Make the CTA a DM CTA."
- "Add one personal-confession line in beat 2."

I preserve what you said to keep; I only change what you asked to change.

## Anti-uses

- Quick hook brainstorm only → `hook-generator.md`.
- Adapt an existing swipe → `remix-generator.md`.

## Links

- Hook generator: [`./hook-generator.md`](./hook-generator.md)
- Remix generator: [`./remix-generator.md`](./remix-generator.md)
- Frameworks: [`../../references/03-story-frameworks.md`](../../references/03-story-frameworks.md)
- Review checklist: [`../../references/99-review-checklist.md`](../../references/99-review-checklist.md)
