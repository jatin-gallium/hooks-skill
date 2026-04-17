# 02 — Hook Taxonomy

STATUS: draft (families are set; examples and swipe-counts will grow from user drops)

Every hook we ingest gets classified into one (sometimes two) of these **pattern families**. When the user drops a swipe, I tag it with 1–2 patterns from this list. When the user wants hooks for an idea, I pull from these families.

## How to read this doc

Each family has:

- **Slug** (used as a tag).
- **Mechanism** — the psychological lever it pulls.
- **Shape** — the structural template.
- **When it works / fails.**
- **Link to `templates/hooks/<slug>.md`** — the fill-in-the-blank template.

## The pattern families

### 1. `curiosity-gap`

- **Mechanism**: open an information loop the reader must close by expanding.
- **Shape**: state a surprising outcome/claim + hide the mechanism.
- **Works**: when the claim is concrete and the hidden piece is genuinely useful.
- **Fails**: when it feels clickbait-y (no payoff) or the gap is too obvious.

### 2. `contrarian-claim`

- **Mechanism**: violate a widely-held belief in the niche.
- **Shape**: "Everyone says X. They're wrong." / "Stop doing X. Do Y instead."
- **Works**: when you actually have the receipts.
- **Fails**: when the "consensus" you attack is a strawman.

### 3. `stat-drop`

- **Mechanism**: a specific, surprising number creates credibility + curiosity.
- **Shape**: "[Surprising number] [unit] [outcome]." + follow-up line.
- **Works**: with unusual precision (`$47,312` > `$47k` > `about $50k`).
- **Fails**: when the stat is vague or stale.

### 4. `personal-confession`

- **Mechanism**: vulnerability + social proof (the creator survived it).
- **Shape**: "I [embarrassing/hard thing]. Here's what I learned."
- **Works**: when the confession is specific and the lesson is portable.
- **Fails**: when it reads as humble-brag.

### 5. `before-after`

- **Mechanism**: transformation arc — shows the delta.
- **Shape**: "[Bad state] → [Good state]. Here's how." Or two contrasting lines.
- **Works**: when both states are concrete and the delta is visible.
- **Fails**: when the "before" is vague or the "after" is unbelievable.

### 6. `list-promise`

- **Mechanism**: tells the reader exactly what they'll get.
- **Shape**: "N [things] that [outcome]." / "The N [X] I wish I knew [when]."
- **Works**: with odd numbers and strong nouns (`7 prompts that…`).
- **Fails**: when the items are generic advice.

### 7. `question-hook`

- **Mechanism**: direct question the reader answers internally.
- **Shape**: single question line, often followed by a second line that reframes it.
- **Works**: when the question triggers a strong internal "yes/no."
- **Fails**: as a vague rhetorical ("Ever wondered…?") — kills reach.

### 8. `storytime-cold-open`

- **Mechanism**: drops the reader into a scene mid-action.
- **Shape**: "It was [time]. [Concrete setting]. [Tension]."
- **Works**: with specific sensory/temporal detail.
- **Fails**: when it meanders before the tension hits.

### 9. `bold-declaration`

- **Mechanism**: a short, punchy, confident statement.
- **Shape**: one-line manifesto. Often 3–8 words.
- **Works**: from a creator with authority/context.
- **Fails**: from someone the reader doesn't recognize and without a second line that earns it.

### 10. `how-i-did-it`

- **Mechanism**: implicit case study + outcome promise.
- **Shape**: "How I [specific outcome] in [timeframe] with [constraint]."
- **Works**: with a specific, quantified outcome.
- **Fails**: when the outcome is soft ("grew my brand").

### 11. `pattern-interrupt`

- **Mechanism**: breaks expected LinkedIn tone — unusually blunt, weird formatting, unexpected word.
- **Shape**: varies; the point is the feed-scroll disruption.
- **Works**: when it matches the creator's voice.
- **Fails**: when it reads as try-hard.

### 12. `stakes-or-warning`

- **Mechanism**: loss-aversion; "you're making a mistake right now."
- **Shape**: "If you're doing X, you're [negative outcome]."
- **Works**: when the X is specific and common.
- **Fails**: when it feels fear-mongery without evidence.

### 13. `insider-reveal`

- **Mechanism**: promise of non-obvious knowledge from behind the curtain.
- **Shape**: "Here's what [role/company] don't tell you about [topic]."
- **Works**: with credible insider position.
- **Fails**: when the "reveal" is common knowledge.

### 14. `one-weird-reframe`

- **Mechanism**: redefines a familiar concept in a surprising way.
- **Shape**: "[Common thing] isn't [common framing]. It's [new framing]."
- **Works**: when the new framing is genuinely useful and portable.
- **Fails**: when it's wordplay without substance.

### 15. `list-of-mistakes`

- **Mechanism**: negative listicle — easier to engage with ("am I doing this?").
- **Shape**: "N [things] killing your [outcome]."
- **Works**: when mistakes are specific and common.
- **Fails**: generic scolding.

### 16. `future-pacing`

- **Mechanism**: paints a vivid future state to pull the reader forward.
- **Shape**: "In [timeframe], [bold prediction]. Here's what it means for [reader]."
- **Works**: when tied to a clear action today.
- **Fails**: as pure punditry.

### 17. `authority-drop`

- **Mechanism**: credentials/experience as the proof.
- **Shape**: "I [did X at Y scale] for [Z years]. Here's what I'd tell my younger self."
- **Works**: sparingly, with real credentials.
- **Fails**: when it's the whole post's value prop.

### 18. `us-vs-them`

- **Mechanism**: identify an in-group; validate their worldview.
- **Shape**: "[Group] know this. [Other group] don't."
- **Works**: when the in-group is clearly defined and positive.
- **Fails**: when it feels exclusionary in a cheap way.

### 19. `frame-the-frame`

- **Mechanism**: meta-hook — tells the reader how to read the post.
- **Shape**: "Save this. / Read this twice. / This is the only post you need about [X]."
- **Works**: when the content genuinely earns it.
- **Fails**: almost always when the content doesn't.

### 20. `specific-moment`

- **Mechanism**: anchors the reader in a precise moment in time.
- **Shape**: "[Exact date/time/context]. [What happened]."
- **Works**: because specificity = credibility.
- **Fails**: when the moment isn't actually relevant to the lesson.

## How patterns combine

Most great hooks use **one dominant pattern + one supporting pattern**. Examples:

- `stat-drop` + `curiosity-gap` — "We closed $1.2M in 14 days. The first 3 days did 80% of it."
- `contrarian-claim` + `insider-reveal` — "Most sales advice is wrong. Here's what actually works at $10M+."
- `storytime-cold-open` + `stakes-or-warning` — "Monday, 9:02am. My biggest client was about to fire us."

I always tag with the **dominant** first, supporting second.

## Links

- Each family's template lives at `../templates/hooks/<slug>.md` (generated as patterns are confirmed by swipes).
- Swipe index: [`../database/swipe.index.md`](../database/swipe.index.md).
- How to choose a pattern for your idea: [`../templates/generators/hook-generator.md`](../templates/generators/hook-generator.md).
