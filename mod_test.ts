import { sparkleOfLove } from "./mod.ts";

// The bytes every port is tested against, so the texts cannot drift.
const EXPECTED_HEX =
  "e29ca8e29da4efb88f20537061726b6c65206f66204c6f766520e29da4efb88fe29ca8";

Deno.test("sparkleOfLove returns the shared bytes", () => {
  const hex = Array.from(new TextEncoder().encode(sparkleOfLove()))
    .map((b) => b.toString(16).padStart(2, "0"))
    .join("");
  if (hex !== EXPECTED_HEX) {
    throw new Error(`sparkleOfLove() bytes = ${hex}, want ${EXPECTED_HEX}`);
  }
});
