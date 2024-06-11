#!/bin/bash

# Detect OS and set paths accordingly
if [[ "$OSTYPE" == "linux-gnu"* || "$OSTYPE" == "darwin"* ]]; then
    # Unix-like system
    VENV_ACTIVATE="$(dirname "$0")/venv_ui/bin/activate"
else
    # Windows system
    VENV_ACTIVATE="$(dirname "$0")/venv_ui/Scripts/activate"
fi

REQUIREMENTS_FILE="$(dirname "$0")/Scripts/requirements_no_ui.txt"
RUN_SCRIPT_FILE="$(dirname "$0")/Scripts/Run_Inference_NO_UI.py"

# Check if venv_ui folder exists in the root directory
if [ ! -d "$(dirname "$0")/venv_no_ui" ]; then
    echo "Creating virtual environment..."
    # Create a virtual environment named "venv_ui" in the root directory
    if [[ "$OSTYPE" == "linux-gnu"* || "$OSTYPE" == "darwin"* ]]; then
        python3 -m venv "$(dirname "$0")/venv_ui"
    else
        python -m venv "$(dirname "$0")/venv_ui"
    fi
fi


echo "Activating the virtual environment..."
# Activate the virtual environment
source "$VENV_ACTIVATE"

echo "Installing requirements..."
# Install requirements inside the virtual environment
pip install -r "$REQUIREMENTS_FILE"

# Export the Hugging Face Read Token as an environment variable
export HUGGINGFACE_READ_TOKEN

echo "Running Python script..."
# Run your Python file here
python "$RUN_SCRIPT_FILE"

echo "Deactivating the virtual environment..."
# Deactivate the virtual environment
deactivate

echo "Script execution complete."
echo "Press Enter to exit..."
read
