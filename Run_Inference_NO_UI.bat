@echo off

set /p sd_model="Enter the Stable Diffusion Model Version (2/xl, xl understands better prompts): "
set /p prompt="Enter your prompt: "
set /p num_inference_steps="Enter the number of inference steps (more integer value = better but longer process: "
set /p guidance_scale="Enter the guidance scale (how much the output is adherent to the prompt) : "
set /p num_images_per_prompt="Enter the number of images per prompt: "
set /p model_precision_type="Enter the model precision type (fp16 which is faster or fp32 which is more precise): "
set /p seed="Enter the seed (A starting point to initiate the generation process, put an integer or 0 for random): "
set /p filename="Enter the output filename with .pgn extension: "
set /p verbose="Produce Verbose (detailed) Output? (y/n): "


if /i "%sd_model%"=="2" (
    set sd_model_version=minecraft-skins
) elif /i "%sd_model%"=="xl" (
    set sd_model_version=minecraft-skins-sdxl
)


if /i "%verbose%"=="y" (
    set verbose_flag=--verbose
) else (
    set verbose_flag=
)


python Python_Scripts/%sd_model_version%.py "%prompt%" %num_inference_steps% %guidance_scale% %num_images_per_prompt% %model_precision_type% %seed% "%filename%" %verbose_flag%

pause