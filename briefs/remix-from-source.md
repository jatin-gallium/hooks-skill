# Brief — Remix From a Source Hook

Use when you saw a hook (in the database or elsewhere) and want it re-angled for your situation.

## Pre-fills

- **Best formats**: Whatever format the source hook used — the point is to preserve the mechanism, swap the surface.
- **Angle bias**: Keep pattern + structure + rules. Swap actor, metric, stakes, villain, jargon, artifact.
- **Rules to emphasize**: Whatever rules the source hook cited.
- **Register**: Default to the target author's register, not the source's.

## Brief

```
BRIEF: remix-from-source

## Source

- Source hook id (from database, e.g. `0025`): <<...>>
  — OR —
  Paste source hook text verbatim here:
  <<...>>

- Source format: <<Dense | Punchy+Context | Single-Line Bomb | Stacked>>
- Rules cited by source: <<list from the source hook's file>>

## Target

- My raw material to swap in:
  - Actor (who the post is about): <<...>>
  - Metric / number: <<...>>
  - Stakes: <<...>>
  - Villain / opposing force / mainstream view: <<...>>
  - Artifact / tool / object: <<...>>
  - Niche: <<#tag>>
  - Audience: <<B2B | personal-brand>>

## Author voice

- Register: <<standard | lowercase>>
- Voice notes:
  <<...>>

## What must NOT change from the source

- Format: <<keep | swap to X>>
- Structural rhythm (line count, where the cliff / cut-off lands): <<keep>>
- Rules the source relies on: <<keep>>

## Constraints

- Must NOT be a line-for-line copy.
- No shared phrasing longer than 3 words with the source (except filler words).
- No em dashes.

## Output request

Generate 5–8 remix hooks preserving format + rules + structural rhythm.
Annotate each: "pattern preserved: <what>, surface swap: <what>".
Recommend top 3.
```

## How to use this brief well

- **A good remix = same pattern, new surface.** If the pattern was Rule 2 + Rule 37 cliffhanger, the remix must also hit those two.
- **Don't swap the format unless the raw material demands it.** If the source was a Punchy+Context and yours becomes a Dense, you've lost what made the source work.
- **Test it against the source.** Read both out loud. They should feel like cousins, not twins.
- **Examples to study**:
  - Any hook in [`../database/hooks/`](../database/hooks/) — pick one, brief it here, and generate variants.
  - Rule cross-reference: [`../database/by-rule/`](../database/by-rule/) to find every hook that uses the rules you want to preserve.
