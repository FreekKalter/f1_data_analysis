#!/bin/bash
if [[ -d ./venv ]]; then
    source ./venv/bin/activate
    jupyter notebook --no-browser
else
    python3 -m venv "$(pwd)/venv"
    source ./venv/bin/activate
    pip -m pip install --upgrade pip
    pip -m pip install -r ./requirements.txt
    jupyter notebook --no-browser
fi
