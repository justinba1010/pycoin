#!/usr/bin/bash

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd -P)"

echo "This could be dangerous if this were real."
read -p "Are you sure? Y/n" -n 1 -r

if [[ $REPLY =~ ^[Yy]$ ]]
then
  pushd $SCRIPT_DIR/../
    rm -rf ./keys/*
  popd
else
  echo "\nGlad you take this seriously."
fi
