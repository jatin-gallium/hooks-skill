#!/usr/bin/env python3
"""
Parse EXAMPLES.md into an atomic, tagged database of hooks.

Emits:
- database/hooks/<NNNN>-<slug>.md  (one file per hook, YAML front-matter + raw text)
- database/hooks.index.md          (master searchable table)
- database/creators/<slug>.md      (per-creator index + voice notes)
- database/by-format/<format>.md   (per-format index)
- database/by-rule/<rule>.md       (per-rule reverse index)

Re-runnable. Idempotent by hook id (sequential, stable across runs as long as
EXAMPLES.md ordering is preserved).
"""

from __future__ import annotations

import os
import re
import sys
from collections import defaultdict
from dataclasses import dataclass, field
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
EXAMPLES = ROOT / "EXAMPLES.md"
DB = ROOT / "database"

FORMAT_RE = re.compile(r"^## FORMAT (\d+): (.+?) \((\d+) hooks\)\s*$")
CREATOR_RE = re.compile(r"^### (.+?)\s*$")
HOOK_NUM_RE = re.compile(r"^\*\*Hook (\d+):\*\*\s*$")
WIDTH_RE = re.compile(r"^Width:\s*(.+?)\s*\|\s*Lines on mobile:\s*(\d+)\s*$", re.IGNORECASE)
WHY_RE = re.compile(r"^Why it works:\s*(.+?)\s*$", re.IGNORECASE)
RULE_REF_RE = re.compile(r"Rule\s+(\d+)")
SEP = "---"

FORMAT_SLUGS = {
    "DENSE": "dense",
    "PUNCHY + CONTEXT": "punchy-context",
    "SINGLE-LINE BOMB": "single-line-bomb",
    "STACKED QUOTES / LIST HOOK": "stacked",
}


def slugify(s: str) -> str:
    s = s.lower()
    s = re.sub(r"[^a-z0-9]+", "-", s).strip("-")
    return s[:60] or "untitled"


@dataclass
class Hook:
    gid: int                       # global sequential id across file
    format_num: int
    format_name: str
    format_slug: str
    creator: str
    creator_slug: str
    hook_num_in_creator: int       # position within this creator block
    text: str                      # raw hook text, preserved exactly
    width_raw: str = ""
    lines_mobile: int | None = None
    why: str = ""
    rules: list[int] = field(default_factory=list)
    char_count: int = 0
    line_count: int = 0

    @property
    def file_id(self) -> str:
        return f"{self.gid:04d}"

    @property
    def title_slug(self) -> str:
        first_line = self.text.splitlines()[0] if self.text else ""
        return slugify(first_line)[:50] or "hook"

    @property
    def filename(self) -> str:
        return f"{self.file_id}-{self.creator_slug}-{self.title_slug}.md"


def parse() -> list[Hook]:
    text = EXAMPLES.read_text(encoding="utf-8")
    lines = text.splitlines()

    hooks: list[Hook] = []
    format_num = 0
    format_name = ""
    format_slug = ""
    creator = ""
    creator_slug = ""
    gid = 0

    i = 0
    n = len(lines)
    while i < n:
        line = lines[i]

        m = FORMAT_RE.match(line)
        if m:
            format_num = int(m.group(1))
            format_name = m.group(2).strip()
            format_slug = FORMAT_SLUGS.get(format_name.upper(), slugify(format_name))
            i += 1
            continue

        m = CREATOR_RE.match(line)
        if m:
            creator = m.group(1).strip()
            creator_slug = slugify(creator)
            i += 1
            continue

        m = HOOK_NUM_RE.match(line)
        if m and format_num and creator:
            hook_num = int(m.group(1))
            i += 1

            body_lines: list[str] = []
            while i < n:
                s = lines[i]
                if WIDTH_RE.match(s) or WHY_RE.match(s):
                    break
                if s.strip() == SEP or HOOK_NUM_RE.match(s) or CREATOR_RE.match(s) or FORMAT_RE.match(s):
                    break
                if s.strip() == "":
                    j = i + 1
                    while j < n and lines[j].strip() == "":
                        j += 1
                    if j >= n:
                        break
                    nxt = lines[j]
                    if WIDTH_RE.match(nxt) or WHY_RE.match(nxt) or nxt.strip() == SEP or HOOK_NUM_RE.match(nxt) or CREATOR_RE.match(nxt) or FORMAT_RE.match(nxt):
                        break
                    body_lines.append("")
                    i = j
                    continue
                body_lines.append(s)
                i += 1

            while body_lines and body_lines[-1].strip() == "":
                body_lines.pop()

            raw_text = "\n".join(body_lines)

            width_raw = ""
            lines_mobile: int | None = None
            why = ""
            rules: list[int] = []

            while i < n:
                s = lines[i]
                if s.strip() == "":
                    i += 1
                    continue
                if s.strip() == SEP or HOOK_NUM_RE.match(s) or CREATOR_RE.match(s) or FORMAT_RE.match(s):
                    break
                wm = WIDTH_RE.match(s)
                if wm:
                    width_raw = wm.group(1).strip()
                    try:
                        lines_mobile = int(wm.group(2))
                    except ValueError:
                        lines_mobile = None
                    i += 1
                    continue
                ym = WHY_RE.match(s)
                if ym:
                    why = ym.group(1).strip()
                    rules = sorted({int(x) for x in RULE_REF_RE.findall(why)})
                    i += 1
                    continue
                i += 1

            gid += 1
            h = Hook(
                gid=gid,
                format_num=format_num,
                format_name=format_name,
                format_slug=format_slug,
                creator=creator,
                creator_slug=creator_slug,
                hook_num_in_creator=hook_num,
                text=raw_text,
                width_raw=width_raw,
                lines_mobile=lines_mobile,
                why=why,
                rules=rules,
                char_count=len(raw_text),
                line_count=len([ln for ln in raw_text.splitlines()]),
            )
            hooks.append(h)
            continue

        i += 1

    return hooks


def write_hook_file(h: Hook) -> Path:
    out = DB / "hooks" / h.filename
    fm = [
        "---",
        f"id: {h.file_id}",
        f"creator: \"{h.creator}\"",
        f"creator_slug: {h.creator_slug}",
        f"format: \"{h.format_name}\"",
        f"format_slug: {h.format_slug}",
        f"format_num: {h.format_num}",
        f"hook_num_in_creator: {h.hook_num_in_creator}",
        f"char_count: {h.char_count}",
        f"line_count: {h.line_count}",
        f"lines_mobile: {h.lines_mobile if h.lines_mobile is not None else 'null'}",
        f"width_raw: \"{h.width_raw}\"",
        f"rules: [{', '.join(str(r) for r in h.rules)}]",
        "source: \"EXAMPLES.md\"",
        "---",
        "",
    ]
    body = [
        f"# {h.file_id} — {h.creator} (Hook {h.hook_num_in_creator}, {h.format_name})",
        "",
        "## Raw hook",
        "",
        "```raw",
        h.text,
        "```",
        "",
        "## Annotations",
        "",
        f"- **Format**: `{h.format_slug}`",
        f"- **Creator**: {h.creator}",
        f"- **Characters**: {h.char_count}",
        f"- **Lines (raw)**: {h.line_count}",
        f"- **Lines on mobile (source)**: {h.lines_mobile if h.lines_mobile is not None else 'n/a'}",
        f"- **Width (source)**: {h.width_raw or 'n/a'}",
        f"- **Rules cited**: {', '.join(f'Rule {r}' for r in h.rules) if h.rules else 'none'}",
        "",
        "## Why it works",
        "",
        h.why or "_not annotated in source_",
        "",
        "## Cross-links",
        "",
        f"- Format index: [`../by-format/{h.format_slug}.md`](../by-format/{h.format_slug}.md)",
        f"- Creator index: [`../creators/{h.creator_slug}.md`](../creators/{h.creator_slug}.md)",
    ]
    if h.rules:
        body.append("- Rules: " + ", ".join(f"[`../by-rule/rule-{r:02d}.md`](../by-rule/rule-{r:02d}.md)" for r in h.rules))
    body.append(f"- Skill spec: [`../../SKILL.md`](../../SKILL.md)")
    body.append(f"- Examples source: [`../../EXAMPLES.md`](../../EXAMPLES.md)")
    body.append("")

    out.write_text("\n".join(fm) + "\n".join(body), encoding="utf-8")
    return out


def write_master_index(hooks: list[Hook]) -> None:
    lines = [
        "# Hooks — Master Index",
        "",
        f"Auto-generated from [`../EXAMPLES.md`](../EXAMPLES.md) via [`../scripts/build_db.py`](../scripts/build_db.py). Do not edit by hand.",
        "",
        f"- Total hooks: **{len(hooks)}**",
        f"- Creators: **{len({h.creator for h in hooks})}**",
        "",
        "## Filter quick-refs",
        "",
        "- By format: [`by-format/`](by-format/)",
        "- By creator: [`creators/`](creators/)",
        "- By rule: [`by-rule/`](by-rule/)",
        "",
        "## Full table",
        "",
        "| id | format | creator | chars | lines | rules | file |",
        "|----|--------|---------|-------|-------|-------|------|",
    ]
    for h in hooks:
        rules_s = ", ".join(str(r) for r in h.rules)
        lines.append(
            f"| {h.file_id} | {h.format_slug} | {h.creator} | {h.char_count} | {h.line_count} | {rules_s} | [{h.filename}](hooks/{h.filename}) |"
        )
    (DB / "hooks.index.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def write_by_format(hooks: list[Hook]) -> None:
    by_fmt: dict[str, list[Hook]] = defaultdict(list)
    for h in hooks:
        by_fmt[h.format_slug].append(h)
    for fmt_slug, items in by_fmt.items():
        fmt_name = items[0].format_name
        lines = [
            f"# Format — {fmt_name} ({len(items)} hooks)",
            "",
            f"See format rules in [`../../SKILL.md`](../../SKILL.md).",
            "",
            "| id | creator | chars | lines | rules | hook preview | file |",
            "|----|---------|-------|-------|-------|--------------|------|",
        ]
        for h in items:
            preview = h.text.replace("\n", " ⏎ ")
            preview = (preview[:80] + "…") if len(preview) > 80 else preview
            preview = preview.replace("|", "\\|")
            rules_s = ", ".join(str(r) for r in h.rules)
            lines.append(
                f"| {h.file_id} | {h.creator} | {h.char_count} | {h.line_count} | {rules_s} | {preview} | [{h.filename}](../hooks/{h.filename}) |"
            )
        (DB / "by-format" / f"{fmt_slug}.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def write_by_rule(hooks: list[Hook]) -> None:
    by_rule: dict[int, list[Hook]] = defaultdict(list)
    for h in hooks:
        for r in h.rules:
            by_rule[r].append(h)
    rule_list_lines = [
        "# Rules — Reverse Index",
        "",
        "Each rule links to every hook in the database that cites it. Rules themselves are defined in [`../../SKILL.md`](../../SKILL.md).",
        "",
    ]
    for r in sorted(by_rule):
        items = by_rule[r]
        rule_list_lines.append(f"- [Rule {r:02d}]({r:02d}-rule.md) — {len(items)} hook(s)")
        lines = [
            f"# Rule {r:02d} — hooks that cite it",
            "",
            f"See rule definition in [`../../SKILL.md`](../../SKILL.md) (Hook Writing Rules or rule section).",
            "",
            "| id | format | creator | chars | hook preview | file |",
            "|----|--------|---------|-------|--------------|------|",
        ]
        for h in items:
            preview = h.text.replace("\n", " ⏎ ")
            preview = (preview[:80] + "…") if len(preview) > 80 else preview
            preview = preview.replace("|", "\\|")
            lines.append(
                f"| {h.file_id} | {h.format_slug} | {h.creator} | {h.char_count} | {preview} | [{h.filename}](../hooks/{h.filename}) |"
            )
        (DB / "by-rule" / f"rule-{r:02d}.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    (DB / "by-rule" / "README.md").write_text("\n".join(rule_list_lines) + "\n", encoding="utf-8")


def write_creators(hooks: list[Hook]) -> None:
    by_creator: dict[str, list[Hook]] = defaultdict(list)
    for h in hooks:
        by_creator[h.creator_slug].append(h)
    index_lines = [
        "# Creators — Index",
        "",
        f"{len(by_creator)} creators across {len(hooks)} hooks.",
        "",
        "| creator | hooks | formats used |",
        "|---------|-------|---------------|",
    ]
    for slug, items in sorted(by_creator.items()):
        creator = items[0].creator
        fmts = sorted({h.format_slug for h in items})
        index_lines.append(f"| [{creator}]({slug}.md) | {len(items)} | {', '.join(fmts)} |")
        lines = [
            f"# {creator}",
            "",
            f"Hooks by {creator} in the database.",
            "",
            "## Counts",
            "",
            f"- Total hooks: **{len(items)}**",
            f"- Formats used: {', '.join(sorted({h.format_slug for h in items}))}",
            "",
            "## Hooks",
            "",
            "| id | format | chars | lines | rules | preview | file |",
            "|----|--------|-------|-------|-------|---------|------|",
        ]
        for h in items:
            preview = h.text.replace("\n", " ⏎ ")
            preview = (preview[:80] + "…") if len(preview) > 80 else preview
            preview = preview.replace("|", "\\|")
            rules_s = ", ".join(str(r) for r in h.rules)
            lines.append(
                f"| {h.file_id} | {h.format_slug} | {h.char_count} | {h.line_count} | {rules_s} | {preview} | [{h.filename}](../hooks/{h.filename}) |"
            )
        (DB / "creators" / f"{slug}.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    (DB / "creators" / "README.md").write_text("\n".join(index_lines) + "\n", encoding="utf-8")


def main() -> int:
    if not EXAMPLES.exists():
        print(f"EXAMPLES.md not found at {EXAMPLES}", file=sys.stderr)
        return 1
    for sub in ("hooks", "by-format", "by-rule", "creators"):
        (DB / sub).mkdir(parents=True, exist_ok=True)
    hooks = parse()
    if not hooks:
        print("No hooks parsed — parser may be mis-aligned with EXAMPLES.md.", file=sys.stderr)
        return 2
    for h in hooks:
        write_hook_file(h)
    write_master_index(hooks)
    write_by_format(hooks)
    write_by_rule(hooks)
    write_creators(hooks)
    print(f"Parsed {len(hooks)} hooks from {EXAMPLES.name}")
    print(f"- hooks/: {len(list((DB / 'hooks').glob('*.md')))} files")
    print(f"- creators/: {len(list((DB / 'creators').glob('*.md')))} files")
    print(f"- by-format/: {len(list((DB / 'by-format').glob('*.md')))} files")
    print(f"- by-rule/: {len(list((DB / 'by-rule').glob('*.md')))} files")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
