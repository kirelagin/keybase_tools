with import <nixpkgs> {};

stdenv.mkDerivation rec {
  name = "keybase-tools";

  src = ./.;

  buildInputs = with python3Packages; [
    python3
    requests2
    scrypt
  ];
}
