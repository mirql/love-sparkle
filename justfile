# love-sparkle: a tiny sparkle of love, the same text in TypeScript, Rust, Python and Go. See README.md.
# (mirql conventions 2026-11-19)

default:
    @just --list

# The gate CI runs: offline, no secrets. Every port's tests, then the secret scan
check: test-ts test-rust test-python test-go secret-scan
    @echo "check: ok"

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
