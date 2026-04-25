# Briefs — reusable hook-writing briefs

A **brief** is a pre-filled context packet you hand to the skill (or to yourself) before asking for hooks. It tells the skill exactly what the post is, what the raw material is, what register to use, and what format/angle bias you want.

Why briefs exist: the skill in [`../SKILL.md`](../SKILL.md) already asks the right questions when you hand it a topic. A brief just pre-answers them so you can batch-generate hooks faster, consistently, across many posts.

## How to use a brief

1. Open the brief that matches the post type.
2. Copy it into a chat (or the skill invocation).
3. Fill in every `<<...>>` placeholder. Do not leave any blank.
4. Optionally override `Format bias`, `Register`, or `Rules to emphasize` based on the situation.
5. Send it to the skill. The skill will output 8–10 hooks per [`../SKILL.md`](../SKILL.md) output format.

## The briefs

| Post type                  | Brief                                               | When to use                                                |
| -------------------------- | --------------------------------------------------- | ---------------------------------------------------------- |
| Data / research / framework| [`data-framework-post.md`](./data-framework-post.md)| You have a number, a stat, a finding, a named framework.   |
| Personal narrative         | [`personal-narrative-post.md`](./personal-narrative-post.md) | Founder story, career pivot, belief-change, life moment. |
| Announcement / launch      | [`announcement-launch-post.md`](./announcement-launch-post.md) | New product, event, cohort, feature.                       |
| Thought leadership / opinion| [`thought-leadership-post.md`](./thought-leadership-post.md) | Hot take, contrarian claim, industry prediction.           |
| Sponsored / partnership    | [`sponsored-partnership-post.md`](./sponsored-partnership-post.md) | Paid post, brand partnership, affiliate.                   |
| Case study / receipts      | [`case-study-post.md`](./case-study-post.md)        | Client win, specific result with numbers.                  |
| Teardown / analysis        | [`teardown-post.md`](./teardown-post.md)            | Analyzing a public artifact (post, ad, launch, company).   |
| Listicle (split list)      | [`listicle-post.md`](./listicle-post.md)            | N things that…, N mistakes, N wins + N losses.             |
| Acknowledgment / gratitude | [`acknowledgment-post.md`](./acknowledgment-post.md)| Shout-out to a group, community thanks.                    |
| Remix from a source hook   | [`remix-from-source.md`](./remix-from-source.md)    | You saw a hook you liked and want it re-angled.            |

## Universal "how to use it well"

The best briefs have three properties:

1. **Concrete raw material** — at least one number, scene, or contrarian claim. "I want to post about sales" is not enough. "We closed $1.2M in 14 days, first 3 days did 80%" is enough.
2. **Explicit register** — `standard` for B2B, `lowercase` only if the author is established in that voice.
3. **Ruthless about what to cut** — name the pieces that are boring. The hook should almost always come from what you almost didn't include.

See [`../SKILL.md`](../SKILL.md) sections "Post Type Hook Angles" and "Register and Tone" for why each brief is shaped the way it is.
