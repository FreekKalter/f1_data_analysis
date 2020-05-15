#!/bin/bash
if [[ -d ./venv ]]; then
    source ./venv/bin/activate
    if [[ $1 != "--no-update" ]]; then
        python ./prepcsv/lib/prepcsv.py
    fi
    jupyter notebook --no-browser
else
    python3 -m venv "$(pwd)/venv"
    source ./venv/bin/activate
    python -m pip install --upgrade pip
    python -m pip install -r ./requirements.txt
    python ./prepcsv/lib/prepcsv.py
    jupyter notebook --no-browser
fi
