# INTAKE — Adding new hooks to the database

The database ([`../database/`](../database/)) is generated from [`../EXAMPLES.md`](../EXAMPLES.md) via [`../scripts/build_db.py`](../scripts/build_db.py). To add new hooks, edit EXAMPLES.md and re-run the parser. This keeps EXAMPLES.md as the single source of truth and the database as a derived index.

## Workflow (single or batch)

1. Open [`../EXAMPLES.md`](../EXAMPLES.md).
2. Find the right `## FORMAT <N>: ...` section (Dense, Punchy + Context, Single-Line Bomb, Stacked).
3. Find or add a `### <Creator Name>` subsection.
4. Append a new hook block using the exact shape below.
5. Bump the `(<N> hooks)` count in the format heading.
6. Run `python3 scripts/build_db.py` from the repo root.
7. Commit EXAMPLES.md + regenerated `database/` together.

## Exact hook block shape

```
**Hook N:**
<verbatim hook text, preserving line breaks>

Width: <source width description> | Lines on mobile: <int>
Why it works: Rule X (note) + Rule Y (note)

---
```

Rules cited must reference rules that exist in [`../SKILL.md`](../SKILL.md) "Hook Writing Rules" section. If a new rule is added to SKILL.md, it becomes available for citation here.

## Bulk drop protocol (for when the user says "I'll drop 200 posts")

When you (the user) are dropping raw LinkedIn posts in bulk to build out the database, send them in this shape per post:

```
creator: <name or "unknown">
format: <Dense | Punchy+Context | Single-Line Bomb | Stacked>
engagement: <optional>
rank: <optional>
source: <optional URL>

<raw hook text, exact line breaks>
```

Separate multiple posts with a line of three dashes (`---`).

What the assistant will do per drop:

1. Classify format against SKILL.md rules (fix if the label is wrong).
2. Validate against character/line-count limits; note any violations.
3. Identify 1–3 SKILL.md rules the hook exercises.
4. Append a properly-formatted block to EXAMPLES.md under the right format + creator.
5. Re-run the parser.
6. Commit with a message like `"Add N hooks from <creator> (<format>)"`.

## When a hook exercises a pattern SKILL.md doesn't yet cover

If you drop a hook that uses a technique not reflected in any existing rule in SKILL.md:

1. Flag it in the commit message.
2. Do NOT invent a new rule inside EXAMPLES.md.
3. Instead, propose a new rule for SKILL.md "Hook Writing Rules" section in a separate commit.
4. Once merged, back-fill the hook's "Why it works" citation.

This keeps SKILL.md as the canonical rulebook.

## Validation on every ingest

Before committing, the parser output must show:

- Total hook count increased by the number of hooks added.
- No parse warnings / errors.
- `database/hooks.index.md` reflects the new counts.
- New hook files exist under `database/hooks/`.

If any of those fail, inspect the edit to EXAMPLES.md — the parser is sensitive to the exact block shape above.

## Anti-patterns (don't)

- Don't edit files under `database/` by hand. They are regenerated on every run.
- Don't paraphrase the hook text. Preserve verbatim including punctuation, capitalization, line breaks.
- Don't add rules to EXAMPLES.md's "Why it works" that aren't in SKILL.md.
- Don't skip the `---` separator between hooks.
