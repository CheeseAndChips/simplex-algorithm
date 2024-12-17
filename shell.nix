{ pkgs, inputsFrom }:
pkgs.mkShell {
  inherit inputsFrom;
  packages = [
    (pkgs.python3.withPackages (python-pkgs: with python-pkgs; [
      # select Python packages here
      # matplotlib
      numpy
      tabulate
    ]))
  ];
}
