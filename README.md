# hooks-skill

A workspace for building reusable **skills** — structured, searchable, directly-usable knowledge packs.

## Skills in this repo

- [**linkedin-hooks**](./skills/linkedin-hooks/SKILL.md) — the ultimate playbook for writing LinkedIn hooks, posts, and story frameworks. Niche-agnostic; ships with a tagged swipe database, hook templates, story-framework templates, and generator playbooks.

## What "skill" means here

A skill is a directory with:

- A top-level `SKILL.md` declaring what the skill is for and when to use it.
- A `references/` directory of mental-model + reference docs.
- A `templates/` directory of fill-in-the-blank templates (hooks, stories, generators).
- A `database/` directory of real examples indexed by tags.
- An `examples/` directory of worked end-to-end uses.

The design goal: you enter from any layer (an idea, a pattern, a framework, a real swipe) and can navigate to any other in one or two links.

## Repo layout

```
.
├── README.md
└── skills/
    └── linkedin-hooks/
        ├── SKILL.md
        ├── README.md
        ├── references/
        ├── templates/
        │   ├── hooks/
        │   ├── stories/
        │   └── generators/
        ├── database/
        │   ├── swipe.index.md
        │   ├── swipe/
        │   └── entries/
        └── examples/
```

## Contributing

Skills are living documents. Drop content into the right directory, update the matching index, cross-link. See each skill's `SKILL.md` for its intake protocol.
