#!/bin/bash

# Get the directory of this script
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"

# Path to the virtual environment
VENV_PATH="$SCRIPT_DIR/venv"

# Function to run pip silently
run_pip_silently() {
    pip "$@" > /dev/null 2>&1
}

# Check if virtual environment exists, if not create it
if [ ! -d "$VENV_PATH" ]; then
    python3 -m venv "$VENV_PATH" > /dev/null 2>&1
fi

# Activate the virtual environment
source "$VENV_PATH/bin/activate" > /dev/null 2>&1

# Install or upgrade requirements silently
run_pip_silently install -r "$SCRIPT_DIR/requirements.txt" --upgrade

# Run the Python script with all arguments passed to this script
"$VENV_PATH/bin/python" "$SCRIPT_DIR/silence_remover.py" "$@"

# Deactivate the virtual environment
deactivate > /dev/null 2>&1