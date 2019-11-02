#!/bin/bash
python3 -m venv "$(pwd)/venv"
source ./venv/bin/activate
pip install -r ./requirements.txt
