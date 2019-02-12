#!/usr/bin/bash

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd -P)"

echo "This is actually dangerous."
read -p "Are you sure? Y/n" -n 1 -r

if [[ $REPLY =~ ^[Yy]$ ]]
then
  echo 
  read -p "Are you sure? Y/n" -n 1 -r
  if [[ $REPLY =~ ^[Yy]$ ]]
  then
    cd $SCRIPT_DIR/../../
    rm -rf $SCRIPT_DIR/../
    exit
  else
    echo "Glad you take this seriously."
  fi

else
  echo "Glad you take this seriously."
fi
