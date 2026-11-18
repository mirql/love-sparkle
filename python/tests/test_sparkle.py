import doctest
import unittest

import mirql_love_sparkle
from mirql_love_sparkle import SPARKLE_OF_LOVE, sparkle_of_love

# The bytes of the npm package's sparkleOfLove(), so the ports cannot drift.
EXPECTED = bytes.fromhex(
    "e29ca8e29da4efb88f20537061726b6c65206f66204c6f766520e29da4efb88fe29ca8"
).decode("utf-8")


class SparkleTest(unittest.TestCase):
    def test_same_text_as_npm(self):
        self.assertEqual(sparkle_of_love(), EXPECTED)
        self.assertEqual(SPARKLE_OF_LOVE, EXPECTED)

    def test_docstring_example(self):
        self.assertEqual(doctest.testmod(mirql_love_sparkle).failed, 0)


if __name__ == "__main__":
    unittest.main()
