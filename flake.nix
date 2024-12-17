{
  description = "A very basic flake";
  inputs = {
    nixpkgs.url = "github:nixos/nixpkgs?ref=nixos-unstable";
    flake-utils.url = "github:numtide/flake-utils";
  };
  outputs = { self, nixpkgs, flake-utils }:
  let
    pythonshell = import ./shell.nix;
    # docflake = import ./doc/flake.nix;
    # docflakeout = docflake.outputs {
    #   inherit self;
    #   inherit nixpkgs;
    #   inherit flake-utils;
    # };
  in {
    devShell.x86_64-linux = pythonshell {
      pkgs = nixpkgs.legacyPackages.x86_64-linux;
      inputsFrom = [ ]; # [ docflakeout.packages.x86_64-linux.default ];
    };
  };
}
