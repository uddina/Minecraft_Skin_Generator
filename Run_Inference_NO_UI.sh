#!/bin/bash

# Detect OS and set paths accordingly
if [[ "$OSTYPE" == "linux-gnu"* || "$OSTYPE" == "darwin"* ]]; then
    # Unix-like system
    VENV_ACTIVATE="$(dirname "$0")/venv_no_ui/bin/activate"
fi

REQUIREMENTS_FILE="$(dirname "$0")/Scripts/requirements_no_ui.txt"

# Check if venv_no_ui folder exists in the root directory
if [ ! -d "$(dirname "$0")/venv_no_ui" ]; then
    echo "Creating virtual environment..."
    # Create a virtual environment named "venv_no_ui" in the root directory
    if [[ "$OSTYPE" == "linux"* || "$OSTYPE" == "darwin"* ]]; then
        python3 -m venv "$(dirname "$0")/venv_no_ui"
    else
        python -m venv "$(dirname "$0")/venv_no_ui"
    fi
fi


echo "Activating the virtual environment..."
# Activate the virtual environment
source "$VENV_ACTIVATE"

echo "Installing requirements..."
# Install requirements inside the virtual environment
pip install -r "$REQUIREMENTS_FILE"


echo "Running Python script..."

read -p "Enter your prompt: " prompt
read -p "Enter the Stable Diffusion Model Version (2/xl, xl understands better prompts): " sd_model
read -p "Enter the number of inference steps (more integer value = better but longer process): " num_inference_steps
read -p "Enter the guidance scale (how much the output adheres to the prompt): " guidance_scale
read -p "Enter the model precision type (fp16 for faster or fp32 for more precision): " model_precision_type
read -p "Enter the seed (an integer or 0 for random): " seed
read -p "Enter the output filename with .png extension: " filename
read -p "See the skin also as a 3D Model? (y/n): " model_3d
read -p "Produce Verbose (detailed) Output? (y/n): " verbose

if [[ "$sd_model" == "2" ]]; then
    sd_model_version="minecraft-skins"
else
    sd_model_version="minecraft-skins-sdxl"
fi


# Initialize flag variables as empty strings.
verbose_flag=""
model_3d_flag=""

if [[ "$verbose" == "y" ]]; then
    verbose_flag="--verbose"
fi

if [[ "$model_3d" == "y" ]]; then
    model_3d_flag="--model_3d"
fi


python Scripts/"$sd_model_version".py "$prompt" "$num_inference_steps" "$guidance_scale" "$model_precision_type" "$seed" "$filename" "$model_3d_flag" "$verbose_flag"

echo "Deactivating the virtual environment..."
# Deactivate the virtual environment
deactivate

echo "Script execution complete."
echo "Press Enter to exit..."
read
