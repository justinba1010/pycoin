#!/usr/bin/bash

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd -P)"

pushd $SCRIPT_DIR/../src/
python3 -c 'from keys import Keys; keys = Keys(); keys.genkey(); keys.saveToFile(); print("Generated: "+str(keys.getaddresses()[-1]))'
popd
