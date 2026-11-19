"""What the sparkle rules let through and what they stop."""
import unittest

from sparkles import escape, problems


class Rules(unittest.TestCase):
    def test_a_kind_line_passes(self):
        self.assertEqual(problems("octocat", "✨ You are doing better than you think <3 ❤️\n"), [])

    def test_stopped(self):
        for name, text, why in [
            ("octocat", "", "it is empty"),
            ("octocat", "one\ntwo", "one line only"),
            ("octocat", "x" * 281, "at most 280 characters (this one has 281)"),
            ("octocat", "visit https://example.test", "no links"),
            ("octocat", "see www.example.test", "no links"),
            ("octocat", "best shop: cheap.xyz", "no links"),
            ("octocat", "hi @someone", "no @mentions"),
            ("-octocat", "hi", "the file name must be your GitHub name, e.g. sparkles/octocat.txt"),
            ("octo--cat", "hi", "the file name must be your GitHub name, e.g. sparkles/octocat.txt"),
        ]:
            with self.subTest(text=text[:20], name=name):
                self.assertIn(why, problems(name, text))

    def test_the_wall_shows_text_not_markup(self):
        self.assertEqual(escape("<b>hi</b> [x](y) *z* <3"),
                         "&lt;b&gt;hi&lt;/b&gt; \\[x\\]\\(y\\) \\*z\\* &lt;3")


if __name__ == "__main__":
    unittest.main()
