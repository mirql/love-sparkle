# Contributing to love-sparkle

Thanks for helping. The first question for any change: is the text still the same, byte for
byte, in every language? love-sparkle stays tiny: no dependencies, no install scripts.

## Your first PR: share a sparkle

The easiest way in: add your own sparkle of love to the wall, and you are one of our
contributors. No code, no git needed.

1. [Open a new sparkle](https://github.com/mirql/love-sparkle/new/main/sparkles?filename=YOUR-GITHUB-NAME.txt)
   in your browser. GitHub makes a copy (fork) of the repo for you.
2. Name the file after your GitHub name: `sparkles/octocat.txt`.
3. Write one line of kindness, for anyone who reads it.
4. **Propose changes**, then **Create pull request**. In the description, `Part of #14.`
   and a hello are enough; you can delete the rest of the template.

The rules, which `just check` checks:

- One line, at most 280 characters. Emoji and `<3` are welcome.
- No links and no @mentions.
- One sparkle per person, in the file with your name.

And the spirit, which a person checks: **kind, humble, curious**, the way we try to be
in all of mirql. Write something you would be glad to get. No ads, no politics, nothing
about anyone else, nothing private.

We read every sparkle and merge it when it fits. Then we add you to the contributors (✨)
and put your sparkle on the wall in the README.

## Before you start

- **Bugs:** open an issue with the bug template.
- **Features:** open an issue first, so we can agree on the shape before you write code.
- **Security problems:** do not open an issue. See [SECURITY.md](SECURITY.md).

## Development

```bash
nix develop
just check       # the checks a PR must pass
```

## Layout

| path | what |
|---|---|
| `mod.ts`, `mod_test.ts` | TypeScript: `@mirql/love-sparkle` on npm (built by `scripts/build_npm.ts`) and JSR (`deno.json`) |
| `rust/` | Rust: crate `mirql-love-sparkle` |
| `python/` | Python: `mirql-love-sparkle` on PyPI |
| `go/` | Go: the module in `go/`, released by tags `go/vX.Y.Z` |

## Releasing (maintainers)

One version for every package.

1. A PR: `just set-version X.Y.Z`, and the "Unreleased" entries under `## X.Y.Z` in
   `CHANGELOG.md`.
2. After the merge, on an up-to-date `main`: `just release X.Y.Z`. It pushes the tags
   `vX.Y.Z` and `go/vX.Y.Z`; the Go tag is the Go release.
3. Approve the waiting run of the `release` workflow (environment `release`). It
   publishes to npm, JSR, crates.io and PyPI with Trusted Publishing; a failed
   registry's job can be re-run alone.
4. Move our own projects that depend on it to the new version: one small PR each,
   lockfile included.

## Merging a sparkle (maintainers)

1. Read it as a stranger would: kind, no hidden ads, nothing about someone else.
2. Squash-merge, and thank them on the PR.
3. On the PR: `@all-contributors please add @<name> for sparkle`.
4. In a follow-up PR (several sparkles can share one): `just sparkles` puts them on the
   README wall.

## Pull requests

- One change per PR. The PR description starts with `Closes #N.`
- `just check` passes; tests cover the new behaviour.
- A line under "Unreleased" in `CHANGELOG.md` for anything a user would notice.
- We merge with squash: the PR title becomes the commit title, so make it say what changes.
