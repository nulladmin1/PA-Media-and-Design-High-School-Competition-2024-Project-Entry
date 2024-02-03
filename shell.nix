{ pkgs ? import <nixpkgs> {} }:

let
  pythonPkgs = ps: with ps; [
    cv2
    deepface
    kivy
    pandas
    requests
  ];
  python = pkgs.python3.withPackages pythonPkgs;
in python.env
