#!/bin/bash
if [[ -d ./venv ]]; then
    source ./venv/bin/activate
    jupyter notebook --no-browser
else
    python3 -m venv "$(pwd)/venv"
    source ./venv/bin/activate
    python -m pip install --upgrade pip
    python -m pip install -r ./requirements.txt
    jupyter notebook --no-browser
fi
