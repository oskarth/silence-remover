#!/bin/bash

# Get the directory of this script
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"

# Path to the virtual environment
VENV_PATH="$SCRIPT_DIR/venv"

# Check if virtual environment exists, if not create it
if [ ! -d "$VENV_PATH" ]; then
    echo "Setting up virtual environment..."
    python3 -m venv "$VENV_PATH"
    source "$VENV_PATH/bin/activate"
    pip install -r "$SCRIPT_DIR/requirements.txt"
else
    source "$VENV_PATH/bin/activate"
fi

# Run the Python script with all arguments passed to this script
python "$SCRIPT_DIR/silence_remover.py" "$@"

# Deactivate the virtual environment
deactivate