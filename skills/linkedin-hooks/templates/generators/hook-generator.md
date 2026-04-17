# Generator — Hook Generator

**Purpose**: given an idea, produce N LinkedIn hook options, each tagged to a pattern family and mapped to a recommended story framework.

## How to invoke

Say something like:

> "Use hook-generator. Idea: <idea>. Niche: <niche>. I want <N> hooks."

Optionally add:

- `voice: <observational | opinionated | confessional>`
- `length: <short | medium | long>` for the eventual post
- `goal: <reach | list | DMs | saves | shares>` so the CTA later is compatible
- `constraints: <things to avoid / include>`

If any of those are missing, I'll either ask one sharp question or default (observational, medium, reach).

## What I produce

For each hook, I return:

1. **The hook text** (1–3 lines, under the "see more" cutoff).
2. **Pattern tag** — which family it's using (from `references/02-hook-taxonomy.md`).
3. **Recommended framework** — the story shape it sets up (from `references/03-story-frameworks.md`).
4. **Risk flag** — any anti-pattern it's close to (from `references/08-anti-patterns.md`).

## Output format

```
1. [PATTERN] <hook>
   → framework: <framework>   | risk: <none | tag from anti-patterns>

2. [PATTERN] <hook>
   → framework: <framework>   | risk: <...>

...
```

## Coverage rule

When asked for N hooks, I spread across patterns — no more than ~30% from a single family — so you get variety, not variations.

Default mix for N=10 (niche-agnostic):

- 2× `curiosity-gap`
- 2× `contrarian-claim`
- 1× `stat-drop`
- 1× `personal-confession`
- 1× `storytime-cold-open`
- 1× `list-promise`
- 1× `one-weird-reframe`
- 1× `bold-declaration`

If you tell me a voice or goal, I bias the mix. Example: `goal: DMs` biases toward `insider-reveal` and `how-i-did-it`.

## Niche adaptation inside the generator

When you give `niche: <tag>`, I:

- Swap `[ACTOR]`, `[METRIC]`, `[STAKES]`, `[VILLAIN]`, `[ARTIFACT]` to niche-native choices.
- Use plausible numbers / jargon for the niche (flagged if speculative).
- Calibrate voice register to the niche (see `references/06-niche-adaptation.md`).

## How to use the output well

1. Scan the pattern tags first, not the hooks. Pick the **mechanism** you like.
2. Then read the hook under it.
3. Ask for variants of the ones you like: "give me 5 more like #3".
4. When you settle on a hook, say "turn #3 into a full post" → uses `post-generator.md`.

## Anti-uses (don't use this for)

- Rewriting an entire swipe — use `remix-generator.md`.
- Writing a full post — use `post-generator.md` (though hook-generator can be step 1).

## Links

- Patterns: [`../../references/02-hook-taxonomy.md`](../../references/02-hook-taxonomy.md)
- Frameworks: [`../../references/03-story-frameworks.md`](../../references/03-story-frameworks.md)
- Niche swaps: [`../../references/06-niche-adaptation.md`](../../references/06-niche-adaptation.md)
