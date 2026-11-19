<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="assets/logo/love-sparkle-dark.svg">
    <img alt="love-sparkle." src="assets/logo/love-sparkle-light.svg" width="420">
  </picture>
</p>

<p align="center"><b>A tiny sparkle of love: the same text in TypeScript, Rust, Python and Go.</b></p>

<p align="center">
  <a href="https://www.npmjs.com/package/@mirql/love-sparkle"><img alt="npm" src="https://img.shields.io/npm/v/@mirql/love-sparkle"></a>
  <a href="https://jsr.io/@mirql/love-sparkle"><img alt="JSR" src="https://jsr.io/badges/@mirql/love-sparkle"></a>
  <a href="https://crates.io/crates/mirql-love-sparkle"><img alt="crates.io" src="https://img.shields.io/crates/v/mirql-love-sparkle"></a>
  <a href="https://pypi.org/project/mirql-love-sparkle/"><img alt="PyPI" src="https://img.shields.io/pypi/v/mirql-love-sparkle"></a>
  <a href="https://pkg.go.dev/github.com/mirql/love-sparkle/go"><img alt="Go Reference" src="https://pkg.go.dev/badge/github.com/mirql/love-sparkle/go.svg"></a>
  <br>
  <a href="LICENSE"><img alt="License: MIT" src="https://img.shields.io/badge/license-MIT-blue"></a>
  <a href="https://github.com/mirql/love-sparkle/actions/workflows/check.yml"><img alt="check" src="https://github.com/mirql/love-sparkle/actions/workflows/check.yml/badge.svg"></a>
  <a href="#install"><img alt="Dependencies: 0" src="https://img.shields.io/badge/dependencies-0-brightgreen"></a>
  <!-- ALL-CONTRIBUTORS-BADGE:START - Do not remove or modify this section -->
<a href="#contributors"><img alt="All contributors" src="https://img.shields.io/badge/all_contributors-1-orange"></a>
<!-- ALL-CONTRIBUTORS-BADGE:END -->
</p>

<p align="center">&lt;3</p>

A tiny sparkle of love: `✨❤️ Sparkle of Love ❤️✨`, the same text byte for byte in every
language, with zero dependencies.

> [!NOTE]
> love-sparkle is 0.7: one version for every package, zero dependencies. It returns one
> string, and that is all it will ever do.

## Install

| Language | Install | Use |
|---|---|---|
| TypeScript (npm) | `npm install @mirql/love-sparkle` | `import { sparkleOfLove } from "@mirql/love-sparkle"` |
| Deno (JSR) | `deno add jsr:@mirql/love-sparkle` | `import { sparkleOfLove } from "@mirql/love-sparkle"` |
| Rust | `cargo add mirql-love-sparkle` | `mirql_love_sparkle::sparkle_of_love()` |
| Python | `uv add mirql-love-sparkle` | `from mirql_love_sparkle import sparkle_of_love` |
| Go | `go get github.com/mirql/love-sparkle/go` | `lovesparkle.Sparkle()` |

The ports: [`rust/`](rust/), [`python/`](python/), [`go/`](go/).

## Development

```bash
nix develop
just check       # the tests of every port, and a secret scan
```

See [CONTRIBUTING.md](CONTRIBUTING.md). Found a security problem? Please report it
privately: [SECURITY.md](SECURITY.md).

## Contributors

Thanks to everyone who made love-sparkle what it is
([emoji key](https://allcontributors.org/docs/en/emoji-key)):

<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->
<table>
  <tbody>
    <tr>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/askaramirov"><img src="https://avatars.githubusercontent.com/u/59274133?size=80" width="80px" height="80px" alt="Askar Amirov"/><br /><sub><b>Askar Amirov</b></sub></a><br /><a href="https://github.com/mirql/love-sparkle/commits?author=askaramirov" title="Code">💻</a> <a href="https://github.com/mirql/love-sparkle/commits?author=askaramirov" title="Documentation">📖</a> <a href="#design-askaramirov" title="Design">🎨</a> <a href="https://github.com/mirql/love-sparkle/commits?author=askaramirov" title="Tests">⚠️</a> <a href="#infra-askaramirov" title="Infrastructure (Hosting, Build-Tools, etc)">🚇</a> <a href="#maintenance-askaramirov" title="Maintenance">🚧</a> <a href="#ideas-askaramirov" title="Ideas, Planning, & Feedback">🤔</a></td>
    </tr>
  </tbody>
</table>

<!-- markdownlint-restore -->
<!-- prettier-ignore-end -->

<!-- ALL-CONTRIBUTORS-LIST:END -->

Helped in a way that isn't a commit? Comment on any issue or PR:
`@all-contributors please add @name for ideas, review` (and so on).

## License

[MIT](LICENSE)
