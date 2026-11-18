# Changelog

One version for every package (npm, JSR, crates.io, PyPI, Go) since 0.7.0.

## Unreleased

## 0.7.0

- One version for every package. Releases come from GitHub Actions with Trusted
  Publishing (no tokens), after a maintainer approves the run; `just release X.Y.Z` tags
  them. CI: `just check` on main and on PRs labelled `ci`.
- The repo moved to `mirql/love-sparkle`. The Go module path is now
  `github.com/mirql/love-sparkle/go` (first version there v0.1.1); the old path stays at
  v0.1.0 and gets no updates.
- mirql conventions: `just check` runs the tests of all four ports and a secret scan;
  `flake.nix` has the tools; AGENTS.md, CONTRIBUTING.md, SECURITY.md and the GitHub
  templates. A TypeScript test against the same bytes as the other ports.
- `__pycache__` files that were committed by mistake are gone, and ignored.
- The npm package no longer ships leftovers of its test build.

## Before 0.7.0

| Where | Name | Versions |
|---|---|---|
| npm, JSR | `@mirql/love-sparkle` | 0.6.1188, 0.6.11881 |
| crates.io | `mirql-love-sparkle` | 0.1.0 |
| PyPI | `mirql-love-sparkle` | 0.1.0 |
| Go | `github.com/mirql/love-sparkle/go` | v0.1.1 |
| Go (old path) | `github.com/askaramirov/mirql-love-sparkle/go` | v0.1.0 |
