# love-sparkle: a tiny sparkle of love, the same text in TypeScript, Rust, Python and Go. See README.md.
# (mirql conventions 2026-11-19)

default:
    @just --list

# The gate CI runs: offline, no secrets. Every port's tests, then the secret scan
check: test-ts test-rust test-python test-go test-sparkles secret-scan
    @echo "check: ok"

# The sparkle wall: the rules' tests, then every sparkle in sparkles/
test-sparkles:
    cd scripts && PYTHONDONTWRITEBYTECODE=1 python3 -m unittest sparkles_test
    PYTHONDONTWRITEBYTECODE=1 python3 scripts/sparkles.py check

# Write the sparkle wall into README.md (after merging new sparkles)
sparkles:
    PYTHONDONTWRITEBYTECODE=1 python3 scripts/sparkles.py wall

# TypeScript (npm, JSR)
test-ts:
    deno test --no-remote mod_test.ts

# Rust (crates.io)
test-rust:
    cd rust && cargo test --offline --quiet

# Python (PyPI); no __pycache__ in the tree
test-python:
    cd python && PYTHONDONTWRITEBYTECODE=1 PYTHONPATH=src python3 -m unittest discover -s tests

# Go (module in go/)
test-go:
    cd go && go vet ./... && go test ./...

# Fail if a credential is in the git history or in the files as they are now
secret-scan:
    gitleaks git --no-banner --redact --log-level warn .
    gitleaks dir --no-banner --redact --log-level warn .

# The version each package has in this checkout
versions:
    @echo "deno.json (npm, JSR):  $(sed -n -E 's/^  "version": "([^"]*)".*/\1/p' deno.json)"
    @echo "rust/Cargo.toml:       $(sed -n -E '0,/^version = /s/^version = "(.*)"/\1/p' rust/Cargo.toml)"
    @echo "python/pyproject.toml: $(sed -n -E '0,/^version = /s/^version = "(.*)"/\1/p' python/pyproject.toml)"

# Set one version in every package (Go takes it from the tag): just set-version 0.7.0
set-version version:
    #!/usr/bin/env bash
    set -euo pipefail
    v={{version}}
    [[ "$v" =~ ^[0-9]+\.[0-9]+\.[0-9]+$ ]] || { echo "version as X.Y.Z" >&2; exit 1; }
    sed -i -E 's/^(  "version": )"[^"]*"/\1"'"$v"'"/' deno.json
    sed -i -E '0,/^version = /s/^version = ".*"/version = "'"$v"'"/' rust/Cargo.toml python/pyproject.toml
    just versions

# Fail unless every package says this version
check-version version:
    #!/usr/bin/env bash
    set -euo pipefail
    n=$(just versions | awk '{print $NF}' | sort -u)
    [ "$n" = "{{version}}" ] || { echo "not every package says {{version}}:" >&2; just versions >&2; exit 1; }
    echo "every package says {{version}}"

# Tag a release on main: vX.Y.Z publishes npm, JSR, crates.io and PyPI (after approval), go/vX.Y.Z the Go module
release version: (check-version version)
    #!/usr/bin/env bash
    set -euo pipefail
    v={{version}}
    git fetch -q origin
    [ "$(git rev-parse --abbrev-ref HEAD)" = main ] || { echo "release from main" >&2; exit 1; }
    [ -z "$(git status --porcelain)" ] || { echo "uncommitted changes" >&2; exit 1; }
    [ "$(git rev-parse HEAD)" = "$(git rev-parse origin/main)" ] || { echo "main is not origin/main" >&2; exit 1; }
    grep -qx "## $v" CHANGELOG.md || { echo "no '## $v' in CHANGELOG.md" >&2; exit 1; }
    echo "tags v$v and go/v$v on: $(git log --oneline -1)"
    read -r -p "push them? [y/N] " a; [ "$a" = y ] || exit 1
    git tag -a "v$v" -m "love-sparkle $v"
    git tag -a "go/v$v" -m "love-sparkle $v (Go)"
    git push origin "v$v" "go/v$v"
    echo "now approve the run: https://github.com/mirql/love-sparkle/actions/workflows/release.yml"
