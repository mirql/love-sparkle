"""A tiny sparkle of love.

The Python port of the ``@mirql/love-sparkle`` npm package: it holds the exact
same sparkle text, byte for byte.

>>> from mirql_love_sparkle import sparkle_of_love
>>> sparkle_of_love()
'✨❤️ Sparkle of Love ❤️✨'
"""

__all__ = ["SPARKLE_OF_LOVE", "sparkle_of_love"]

SPARKLE_OF_LOVE = "✨❤️ Sparkle of Love ❤️✨"
"""The sparkle of love text, identical to ``sparkleOfLove()`` of the npm package."""


def sparkle_of_love() -> str:
    """Return the sparkle of love text."""
    return SPARKLE_OF_LOVE
