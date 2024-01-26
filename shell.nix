{ pkgs ? import <nixpkgs> {} }:

let
  pythonPkgs = ps: with ps; [
    kivy
    pandas
    requests
    # Surprise:
    (
      buildPythonPackage rec {
        pname = "scikit-surprise";
        version = "1.1.3";
        src = fetchPypi {
          inherit pname version;
          sha256 = "sha256-Vr/sQQshJ4gHt1OKy3QF25m0STclndMpdizufmZ9S8w=";
        };
        doCheck = false;
        propagatedBuildInputs = with pkgs; [
        libgcc
        numpy
        ];
      }
    )
  ];
  python = pkgs.python3.withPackages pythonPkgs;
in python.env
