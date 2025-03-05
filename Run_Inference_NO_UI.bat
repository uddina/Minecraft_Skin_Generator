@echo off
setlocal

REM Check if venv_no_ui folder exists in the root directory and if requirements are installed
if not exist "%~dp0venv_no_ui\" (
    REM Print the step to the terminal
    echo Creating virtual environment...

    REM Create a virtual environment named "venv_no_ui" in the root directory
    python -m venv "%~dp0venv_no_ui"
	
    REM Print the step to the terminal
    echo Activating the virtual environment...

    REM Activate the virtual environment
    call "%~dp0venv_no_ui\Scripts\activate.bat"
	
    REM Print the step to the terminal
    echo Installing requirements...

    REM Install requirements inside the virtual environment
    pip install -r "%~dp0Scripts\requirements_no_ui.txt"
) else (
    echo Required packages are already installed and Virtual environment is already created.
	
    REM Print the step to the terminal
    echo Activating the virtual environment...

    REM Activate the virtual environment
    call "%~dp0venv_no_ui\Scripts\activate.bat"
)

REM Print the step to the terminal
echo Running Python script...


set /p prompt="Enter your prompt: "
set /p sd_model="Enter the Stable Diffusion Model Version (2/xl, xl understands better prompts): "
set /p num_inference_steps="Enter the number of inference steps (more integer value = better but longer process) : "
set /p guidance_scale="Enter the guidance scale (how much the output is adherent to the prompt) : "
set /p model_precision_type="Enter the model precision type (fp16 which is faster or fp32 which is more precise but more resource consuming): "
set /p seed="Enter the seed (A starting point to initiate the generation process, put an integer or 0 for random): "
set /p filename="Enter the output filename with .png extension: "
set /p model_3d="See the skin also as a 3D Model? (y/n): "
set /p verbose="Produce Verbose (detailed) Output? (y/n): "


if /i "%sd_model%"=="2" (
    set sd_model_version=minecraft-skins
) else (
    set sd_model_version=minecraft-skins-sdxl
)

REM Initialize flag variables as empty strings.
set "verbose_flag="
set "model_3d_flag="

if /i "%verbose%"=="y" (
    set verbose_flag=--verbose
)

if /i "%model_3d%"=="y" (
    set model_3d_flag=--model_3d
)


python Scripts/%sd_model_version%.py "%prompt%" %num_inference_steps% %guidance_scale% %model_precision_type% %seed% "%filename%" %model_3d_flag% %verbose_flag%

REM Print the step to the terminal
echo Deactivating the virtual environment...

REM Deactivate the virtual environment
call "%~dp0venv_no_ui\Scripts\deactivate.bat"

REM Print the step to the terminal
echo Script execution complete.

endlocal

pause
