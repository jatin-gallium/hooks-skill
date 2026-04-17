# Niche Remix Protocol

You will read hooks from one niche (e.g. SaaS GTM, content creator economy) and need to adapt them to a different niche (e.g. fitness, finance, recruiting). This doc is the exact procedure.

## The core idea

Every hook has two layers:

- **Mechanism layer** — the format, the rules it cites, the structural rhythm, the rhetorical move. **This is what made the hook work. Preserve it.**
- **Surface layer** — actor, metric, stakes, villain, artifact, jargon, specific numbers. **Swap this entirely per niche.**

A successful remix keeps 100% of the mechanism and 0% of the surface.

## Procedure

1. **Pick the source hook.** Either a database id (e.g. `0028`) or a pasted hook.
2. **Open its database file** to see: `format`, `rules`, `char_count`, `line_count`, structural rhythm.
3. **Name the mechanism in one sentence.** "Large-scale action + specific result + timeframe, single Dense line."
4. **List the surface elements to swap:**
   - **Actor** — who the post is about (founder / rep / creator / lifter / PM / recruiter).
   - **Metric** — niche-native unit ($ARR, close rate, cycle time, PRs, NPS, CTR, retention).
   - **Stakes** — what's on the line (revenue / deal / hire / launch / cert / title).
   - **Villain** — the opposing force or mainstream view (churn / stalled deals / bad hires / plateau / industry orthodoxy).
   - **Artifact** — the concrete object (dashboard / deck / playbook / macro / PR / OKR).
   - **Jargon** — enough to signal belonging, not so much you lock out adjacent readers.
5. **Write 3–5 candidate remixes** using the same format, same rules, same line count, same rhythm.
6. **Validate** each candidate against [`../SKILL.md`](../SKILL.md) (char count, line breaks, banned phrases).
7. **Pick the strongest 3** — usually the one with the most specific number wins.

## Voice register calibration

Even within the same mechanism, register must match the target niche:

| Target niche    | Typical register | Vulnerability tolerance | Numbers precision |
| --------------- | ---------------- | ----------------------- | ----------------- |
| `#founder`      | standard         | high                    | very high         |
| `#sales`        | standard         | medium                  | very high         |
| `#saas`         | standard         | medium                  | very high         |
| `#marketing`    | standard / lowercase (creator-brand) | high | high            |
| `#career`       | lowercase ok     | very high               | medium            |
| `#recruiting`   | standard         | medium                  | medium            |
| `#hr`           | standard         | low-medium              | medium            |
| `#finance`      | standard         | low                     | very high         |
| `#fitness`      | lowercase ok     | high                    | high              |
| `#ai`           | standard         | medium                  | high              |
| `#creator-econ` | lowercase common | high                    | medium            |

See [`../SKILL.md`](../SKILL.md) § Register and Tone for the authoritative rules.

## Common remix failure modes

1. **Format drift.** Source was Punchy+Context (line 1 ≤50, line 2 ≤50). Your remix has 62-char line 1. You broke the format.
2. **Rule drift.** Source cited Rule 2 + Rule 37. Your remix kept Rule 2 but lost the cliffhanger. It's now a weaker hook.
3. **Surface underswap.** You kept "LinkedIn" in the hook when adapting to a fitness niche. Full swap, always.
4. **Surface overswap.** You replaced so much that the rhythm broke. If the source used a specific number, your remix needs a specific number in the same slot.
5. **Register mismatch.** Source was lowercase creator voice. You remixed for enterprise sales in lowercase. Reads careless.

## Example (walkthrough)

**Source** (`database/hooks/0028-*`):

> I built 13,000+ pages with AI in 3 hours and grew my SEO traffic by +466% 60 days later.

- Format: Dense (1 line, ~140 chars)
- Rules: 2 (specific numbers), 7 (time + result metric)
- Mechanism: "[Massive scale action] in [short timeframe] → [outsized result] [delayed timeframe]."

**Remix for `#sales`**:

> I sent 2,400 cold emails in 2 weeks and closed $487K from the ones I almost didn't send.

- Format: Dense (1 line, ~96 chars — a bit short, could be extended to 140-160 per SKILL.md Dense rule)
- Rules preserved: 2, 7 + added Rule 12 (reframe)
- Surface swapped: actor (sales rep), metric (emails + $), timeframe (2 weeks + same-period), artifact (cold emails).

**Remix for `#fitness`**:

> I ran 412 miles in 90 days with a torn meniscus and PR'd my marathon by 18 minutes.

- Format: Dense (~107 chars — needs to be padded to Dense's 140–160 range before output)
- Rules preserved: 2, 7 + added Rule 26 (vulnerability: torn meniscus).
- Surface swapped: actor (runner), metric (miles, minutes), stakes (injury), artifact (marathon).

## Minimum checklist for a valid remix

- [ ] Same format as source (or explicit justified swap).
- [ ] Same rule set cited, ± one substitution max.
- [ ] Char count within format's range (see SKILL.md).
- [ ] No shared 4+ word substring with source (except stopwords).
- [ ] Register matches target niche.
- [ ] Specific number(s) preserved in the same structural slot.

## Links

- Source hooks: [`../database/hooks/`](../database/hooks/)
- Rule cross-index: [`../database/by-rule/`](../database/by-rule/)
- Remix brief: [`../briefs/remix-from-source.md`](../briefs/remix-from-source.md)
