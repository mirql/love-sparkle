package lovesparkle_test

import (
	"encoding/hex"
	"fmt"
	"testing"

	lovesparkle "github.com/askaramirov/mirql-love-sparkle/go"
)

// The bytes of the npm package's sparkleOfLove(), so the ports cannot drift.
const expectedHex = "e29ca8e29da4efb88f20537061726b6c65206f66204c6f766520e29da4efb88fe29ca8"

func TestSameTextAsNpm(t *testing.T) {
	if got := hex.EncodeToString([]byte(lovesparkle.Sparkle())); got != expectedHex {
		t.Fatalf("Sparkle() bytes = %s, want %s", got, expectedHex)
	}
}

func ExampleSparkle() {
	fmt.Println(lovesparkle.Sparkle())
	// Output: ✨❤️ Sparkle of Love ❤️✨
}
