# Contributing to love-sparkle

Thanks for helping. The first question for any change: is the text still the same, byte for
byte, in every language? love-sparkle stays tiny: no dependencies, no install scripts.

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

## Pull requests

- One change per PR. The PR description starts with `Closes #N.`
- `just check` passes; tests cover the new behaviour.
- A line under "Unreleased" in `CHANGELOG.md` for anything a user would notice.
- We merge with squash: the PR title becomes the commit title, so make it say what changes.
