{ pkgs ? import <nixpkgs> {} }:

let
  pythonPkgs = ps: with ps; [
    kivy
    pandas
    requests
    opencv4

    # DeepFace
    (
      buildPythonPackage rec {
        pname = "deepface";
        version = "0.0.83";
        src = fetchPypi {
          inherit pname version;
          sha256 = "sha256-yxpES7KTIVP++3gBb1V7gGmbCFf5uFfNmSgbg2I03O4=";
        };
        doCheck = false;
        propagatedBuildInputs = with pkgs; [
          python311Packages.gunicorn
        ];
      }
    )
  ];
  python = pkgs.python3.withPackages pythonPkgs;
in python.env
