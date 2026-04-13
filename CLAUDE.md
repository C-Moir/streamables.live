# streamables.live — CLAUDE.md

## What This Is
The live source for streamables.live. A personal studio/lab site for Cameron J. Moir.

## Hosting
Domain: Namecheap. Hosting: Hostinger. Deploy: manual upload via Hostinger file manager. No CI/CD.

## Stack
- Zero framework. Pure HTML, CSS, vanilla JS.
- Single file: `index.html` is the entire site.
- No build step. No npm. No bundler. What you edit is what gets deployed.

## Key Files
- `index.html` — the whole site
- `articles/` — real hosted articles (loaded dynamically by the site)
- `projects/` — real hosted project entries
- `shukinkara.html`, `shukinkara-document.html` — Shukinkara project pages
- Image assets (`St-03.png`, icons etc.) in root

## Rules
- Do NOT introduce npm, React, or any build tooling. Intentionally dependency-free.
- Do NOT change the aesthetic — glassmorphism, dark background, `//` comment-style section dividers.
- Australian English in all copy.
- Adding an article = drop a file in `articles/` and update the index reference in `index.html`.
- Adding a project = same pattern in `projects/`.
- After editing, upload changed files via Hostinger file manager.
