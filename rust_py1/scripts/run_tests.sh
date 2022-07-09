#!/usr/bin/env bash

SCRIPTPATH = "$( cd "$(dirname "$0")" ; pwd -P )"
cd $SCRIPTPATH
cd ..
source venv/bin/activate
export PYTHONPATH="./rust_py1"
python3 -m unittest discover