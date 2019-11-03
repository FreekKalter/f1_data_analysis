#!/bin/bash
python3 -m venv "$(pwd)/venv"
source ./venv/bin/activate
pip install --upgrade pip
pip install -r ./requirements.txt
