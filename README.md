<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="assets/logo/love-sparkle-dark.svg">
    <img alt="love-sparkle." src="assets/logo/love-sparkle-light.svg" width="420">
  </picture>
</p>

<p align="center"><b>A tiny sparkle of love: the same text in TypeScript, Rust, Python and Go.</b></p>

<p align="center">&lt;3</p>

A tiny sparkle of love: `✨❤️ Sparkle of Love ❤️✨`, the same text byte for byte in every
language, with zero dependencies.

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

## License

[MIT](LICENSE)
