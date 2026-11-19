"""The sparkle wall: everyone's sparkle of love, in sparkles/<github-name>.txt.

    python3 scripts/sparkles.py check    # every sparkle follows the rules (just check runs this)
    python3 scripts/sparkles.py wall     # writes the wall into README.md, oldest sparkle first

A sparkle is one line of kindness, at most 280 characters, with no links and no
@mentions. The file is named after its author's GitHub name. The wall is ordered by
when each file was first committed, so the first sparkle stays first.
"""
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
FOLDER = ROOT / "sparkles"
README = ROOT / "README.md"
START = "<!-- SPARKLE-WALL:START - written by `just sparkles`, do not edit -->"
END = "<!-- SPARKLE-WALL:END -->"
MAX = 280
NAME = re.compile(r"^[A-Za-z0-9](?:[A-Za-z0-9]|-(?=[A-Za-z0-9])){0,38}$")  # GitHub's rules for a name
LINK = re.compile(r"(?i)(://|www\.|\.(com|org|net|io|dev|xyz|ru|cn)\b)")


def problems(name: str, text: str) -> list[str]:
    """What is wrong with one sparkle file, or nothing."""
    found = []
    if not NAME.match(name):
        found.append("the file name must be your GitHub name, e.g. sparkles/octocat.txt")
    line = text.strip()
    if not line:
        found.append("it is empty")
    if "\n" in line:
        found.append("one line only")
    if len(line) > MAX:
        found.append(f"at most {MAX} characters (this one has {len(line)})")
    if LINK.search(line):
        found.append("no links")
    if "@" in line:
        found.append("no @mentions")
    return found


def sparkles() -> dict[str, str]:
    return {p.stem: p.read_text(encoding="utf-8").strip() for p in sorted(FOLDER.glob("*"))
            if p.is_file() and p.name != "README.md"}


def order(names: list[str]) -> list[str]:
    """Oldest first, by the commit that added each file; files not committed yet last."""
    log = subprocess.run(["git", "-C", str(ROOT), "log", "--reverse", "--diff-filter=A", "--format=",
                          "--name-only", "--", "sparkles/"], capture_output=True, text=True).stdout
    added = {}
    for path in log.split():
        added.setdefault(Path(path).stem, len(added))
    return sorted(names, key=lambda n: (added.get(n, len(added)), n.lower()))


def escape(line: str) -> str:
    """Plain text in Markdown: no HTML, no formatting, no links."""
    line = line.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
    return re.sub(r"([\\`*_{}\[\]()#+!|~])", r"\\\1", line)


def wall() -> str:
    items = sparkles()
    lines = [f"- {escape(items[n])} · [{n}](https://github.com/{n})" for n in order(list(items))]
    return "\n".join([START, *lines, END])


def check() -> int:
    bad = 0
    for path in sorted(FOLDER.glob("*")):
        if path.name == "README.md":
            continue
        if path.suffix != ".txt" or not path.is_file():
            print(f"{path.relative_to(ROOT)}: only sparkles/<github-name>.txt files here", file=sys.stderr)
            bad += 1
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            print(f"{path.relative_to(ROOT)}: not UTF-8 text", file=sys.stderr)
            bad += 1
            continue
        for p in problems(path.stem, text):
            print(f"{path.relative_to(ROOT)}: {p}", file=sys.stderr)
            bad += 1
    if START not in README.read_text(encoding="utf-8"):
        print("README.md: the sparkle wall markers are missing", file=sys.stderr)
        bad += 1
    print(f"sparkles: {len(sparkles())}, problems: {bad}")
    return 1 if bad else 0


def write_wall() -> int:
    text = README.read_text(encoding="utf-8")
    new = re.sub(re.escape(START) + r".*?" + re.escape(END), lambda _: wall(), text, flags=re.S)
    README.write_text(new, encoding="utf-8")
    print("README.md: wall " + ("updated" if new != text else "already up to date"))
    return 0


if __name__ == "__main__":
    cmd = sys.argv[1] if len(sys.argv) > 1 else ""
    if cmd not in ("check", "wall"):
        sys.exit(__doc__)
    sys.exit(check() if cmd == "check" else write_wall())
