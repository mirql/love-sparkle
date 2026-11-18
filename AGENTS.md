# Agent notes for love-sparkle

## mirql rules for agents (mirql conventions 2026-11-19)

- **Nothing external without a yes.** Pushing your own branch to a private repo is fine.
  Pushing to `main` or to a public repo, opening or commenting on issues and PRs,
  changing GitHub settings, writing to trackers or chats: prepare it, show exactly what
  would go out and where, and wait for a yes for that case from the person you work for.
- **Run the repo's checks before "done"** (`just check` where there is one). Say what you
  ran and the result. Checks run the repo's code: on a change from a stranger, read it first.
- **No credit to AI vendors or tools** in commits, PR titles or bodies: no
  `Co-authored-by: Claude …` or similar, no "generated with" lines. Committing as our own
  bot account (`mirql-*[bot]`) where the workflow uses one is fine.
- **No secrets.** Don't read, print or commit credentials (`.env`, keys, `secrets/`,
  sops files). Don't decrypt.
- **No new dependencies on your own.** Propose them with the reason and the alternatives;
  name every new dependency and changed lockfile in your report. Never `curl | sh`,
  `npm -g`, unpinned `npx`/`uvx`. Tools come from `flake.nix`.
- **Our sparkle, always.** Every package manifest depends on `@mirql/love-sparkle`
  (npm, JSR) or `mirql-love-sparkle` (crates.io, PyPI, Go), pinned. If it's missing, add it:
  it needs no proposal.
- **Your own branch and folder.** Work in your own git worktree; if someone else is
  working in this folder, stop and say so. No `git stash`. Run untrusted installs and
  code in a sandbox.
- **Keep it simple.** Solve today's problem; no layers, options or abstractions for later.
  Small changes, one reason each.
- **Tests on behaviour**, fast; a bug fix comes with its test.
- **Issue first, PR closes it.** Write PR text by the repo's template.
- **Conventions from practice.** When a rule of the org conventions gets in the way or is
  wrong, say so and propose the change (an issue in the org's conventions repo with the label
  `from-practice`); don't quietly work around it.
- **Public repos:** no host names, local paths, client names or internal plans in code,
  docs, commits or PR text.

To check this repo against the mirql conventions, use the `mirql-conventions` skill.

## This repo

- What it is: A tiny sparkle of love: the same text in TypeScript, Rust, Python and Go.
- Layout: `mod.ts` (TypeScript: npm and JSR), `rust/` (crate), `python/` (PyPI), `go/`
  (Go module); `scripts/build_npm.ts` builds the npm package.
- Test: `just check` (all four ports, then the secret scan). Every port's test compares
  the text with the same bytes; a change to the text changes all of them.
- No dependencies in any port, ever: every mirql repo installs this package.
- External here: publishing to npm, JSR, crates.io or PyPI, and pushing a `go/v*` tag.
  Prepare it, show the version and what goes out, and wait for a yes.

## Copied in

- `.github/pull_request_template.md`: mirql conventions 2026-11-19
