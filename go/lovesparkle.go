// Package lovesparkle is a tiny sparkle of love.
//
// It is the Go port of the @mirql/love-sparkle npm package: it holds the exact
// same sparkle text, byte for byte.
package lovesparkle

// SparkleOfLove is the sparkle of love text, identical byte for byte to the one
// produced by the npm package's sparkleOfLove().
const SparkleOfLove = "✨❤️ Sparkle of Love ❤️✨"

// Sparkle returns the sparkle of love text.
func Sparkle() string {
	return SparkleOfLove
}
