{
  description = "love-sparkle: a tiny sparkle of love, the same text in TypeScript, Rust, Python and Go.";

  inputs.nixpkgs.url = "github:NixOS/nixpkgs/nixos-unstable";

  outputs = {nixpkgs, ...}: let
    systems = ["x86_64-linux" "aarch64-linux" "aarch64-darwin" "x86_64-darwin"];
    forAll = f: nixpkgs.lib.genAttrs systems (system: f nixpkgs.legacyPackages.${system});
  in {
    # `nix develop`: everything the justfile needs.
    devShells = forAll (pkgs: {
      default = pkgs.mkShell {
        packages = [
          pkgs.just
          pkgs.gitleaks
          pkgs.deno # TypeScript port, npm build (scripts/build_npm.ts)
          pkgs.cargo # Rust port
          pkgs.rustc
          pkgs.python3 # Python port
          pkgs.uv # Python build and publish
          pkgs.go # Go port
        ];
      };
    });

    formatter = forAll (pkgs: pkgs.alejandra);
  };
}
