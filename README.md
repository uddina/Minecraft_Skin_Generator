# Stable Diffusion Minecraft Skin Generator

[![Discord](https://img.shields.io/discord/1198701940511617164?color=%23738ADB&label=Discord&style=for-the-badge)](https://discord.gg/osai)

## Overview

The process of fine tuning a Stable Diffusion model to generate Minecraft character previews is detailed here: [Digging into Stable Diffusion-Generated Minecraft Skins](https://monadical.com/posts/mincraft-skin-generation.html).

This codebase further refines that model, and allows for in-game skins to be generated using only a text prompt.  The finetuned model for doing so is available on HuggingFace as [monadical-labs/minecraft-skin-generator](https://huggingface.co/monadical-labs/minecraft-skin-generator).  The model development process is described here in a subsequant blog post: [Even More Skin in the Game: Digging Deeper Into Stable Diffusion-Generated Minecraft Skins](https://monadical.com/posts/minecraft-skins-part2.html).

If you want to finetune this model, check [here](https://docs.monadical.com/zzthlWvuSj-PXyN4ZZiCyg#Fine-tuning-the-Stable-Diffusion-model)

## Example

Prompt: "A man in a purple suit wearing a tophat"

Output Image Asset Skin:

![images/purple.png](images/purple.png)

Skin Imported In Game:

![images/minecraft-screenshot.png](images/minecraft-screenshot.png)

# Requirements:
- [Python (3.10.6+)](https://www.python.org/downloads/)
- [ImageMagick (ONLY IF YOU WANNA SEE THE GENERATED SKIN AS 3D MODEL)](https://imagemagick.org/script/download.php)

# Usage

## Local

### Precompiled

1. Click the Code button and download it as a Zip.

2. Extract the .zip file.

3. Now you gotta Inference:

4. Choose which version:

- Windows:

  - UI: Open Run_Inference_UI.bat, let it create the venv_ui and install the requirements. After that ctrl+click the local url.

  - NO UI: Open Run_Inference_NO_UI.bat, let it create the venv_no_ui and install the requirements, it will ask you for the parameters to set that are explained below

- Mac & Linux

  - UI: Open Run_Inference_UI.sh, let it create the venv_ui and install the requirements. After that ctrl+click the local url.

  - NO UI: Open Run_Inference_NO_UI.sh, let it create the venv_no_ui and install the requirements, it will ask you for the parameters to set that are explained below

A: Enter the prompt, so how the Minecraft Skins should look like.

B: Choose the Stable Diffusion Model, either 2 or xl (xl is better).

C: Enter the integer value for the Inference Steps, which is basically denoising the image so an higher value = better output but longer process, it's suggested to use either 25 or 50.

D: Enter the guidance scale, the float value for how much the output is adherent to the prompt, the 'max' is 10.0.

E: Enter the model precision type,fp16 (which is faster) or fp32 (which is more precise but slower and need more resources).

F: Put the Seed, the starting point to initiate the generation process, either an integer value or 0 for a random one, max is 2147483647.

G: Write the Output Image Skin Asset Name with the .png extension.

H: Choose if to see the output as a 3D model too or not, you need [ImageMagick (ONLY IF YOU WANNA SEE THE GENERATED SKIN AS 3D MODEL](https://imagemagick.org/script/download.php) for it (NO UI: y or n / UI: check the box).

I: Choose if to show a verbose (detailed) output or not, not really needed (NO UI: y or n / UI: check the box).

4. About the Outputs, if you are running:
   
- UI: Download output skin asset image by the download icon in the ui version in the web ui when its done making the skin, also you can download the 3d model in .glb format of the skin.
  
- NO UI: The output skin asset image will be saved into the output_minecraft_skins folder with the output name you gave it before, also you will have a (name-you-gave-the-skin)-converted.png which is the skin converted from 64x32 to 64x64 to make it adherent on the 3d model player which are in the files (this bug happened only to this 3d model, the skin asset will work fine in game, you can delete that file if you want to, it's useless and the 3d model will work without it), and also you will find a (name-you-gave-the-skin)_3d_model.glb
  
5. You can import now the skin into Minecraft, which you can do with a slightly different way based on the Minecraft version you play so just google it lol.

## Online

### Website
We have released a hosted version of our Minecraft Skin Generator at: [https://www.skingenerator.io](https://www.skingenerator.io)

While closed source, this version improves on the quality of generated skins from the publicly available model, plus it supports transparency in the helmet/hair section of the skins.  Please check it out and let us know what you think!

### Google Colab

- Run NO UI <a target="_blank" href="https://colab.research.google.com/github/Nick088Official/Stable_Diffusion_Finetuned_Minecraft_Skin_Generator/blob/main/Stable_Diffusion_Finetuned_Minecraft_Skin_Generator_NO_UI.ipynb">
  <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/>
</a>

- Run Ipywidgets UI <a target="_blank" href="https://colab.research.google.com/github/Nick088Official/Stable_Diffusion_Finetuned_Minecraft_Skin_Generator/blob/main/Stable_Diffusion_Finetuned_Minecraft_Skin_Generator_Ipywidgets_UI.ipynb">
  <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/>
</a>

- Run WEB UI **(WARNING: COULD RISK YOUR FREE TIER COLAB ACC)** <a target="_blank" href="https://colab.research.google.com/github/Nick088Official/Stable_Diffusion_Finetuned_Minecraft_Skin_Generator/blob/main/Stable_Diffusion_Finetuned_Minecraft_Skin_Generator_WEB_UI.ipynb">
  <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/>
</a>

### Hugging Face Space

[**YOUTUBE TUTORIAL**](https://www.youtube.com/watch?v=aqAI7_WJkDA)

[Hugging Face Space](https://huggingface.co/spaces/Nick088/Stable_Diffusion_Finetuned_Minecraft_Skin_Generator)

### Kaggle

- [Run NO UI ![Kaggle](https://img.shields.io/badge/Kaggle-035a7d?style=for-the-badge&logo=kaggle&logoColor=white)](https://github.com/Nick088Official/Stable_Diffusion_Finetuned_Minecraft_Skin_Generator/blob/main/kaggle-stable-diffusion-minecraft-skin-generator-no-ui.ipynb)
- [Run Ipywidgets UI ![Kaggle](https://img.shields.io/badge/Kaggle-035a7d?style=for-the-badge&logo=kaggle&logoColor=white)](https://github.com/Nick088Official/Stable_Diffusion_Finetuned_Minecraft_Skin_Generator/blob/main/kaggle-sd-finetuned-minecraft-skin-generator-ipywidgetsui.ipynb)
- [Run WEB UI **(WARNING: YOU COULD RISK YOUR KAGGLE ACCOUNT)** ![Kaggle](https://img.shields.io/badge/Kaggle-035a7d?style=for-the-badge&logo=kaggle&logoColor=white)](https://github.com/Nick088Official/Stable_Diffusion_Finetuned_Minecraft_Skin_Generator/blob/main/kaggle-stable-diffusion-minecraft-skin-generator-web-ui.ipynb)

1. Download one of the 2 Kaggle Notebooks Files above
2. Go on https://kaggle.com, be sure you make an account and are phone verified.
3. Click the '+', then 'Create new notebook'.
4. Click 'File' and 'Import Notebook'.
5. Import the kaggle notebook file.


## Changelog
### Update - October 21th, 2024
Fixed Kaggle & Google Colab Web UI, updated gradio from 4.36.0 to 4.41.0 for fixing localtunnel issues, and update Pillow from 9.0.1 to 10.4.0 to fix incompatibility with python 3.11.
### Update - October 14th, 2024
Added a Youtube Tutorial for the (ZeroGPU) HuggingFace Space.
### Update - September 20th, 2024
Fix typo on the WEB UI Colab.
### Update - June 19th, 2024
Kaggle Notebook Files.
### Update - June 12-13th, 2024
Fixed UI Inference py script, fixed no ui shell script, adjusted the ui parameters.
### Update - June 11th, 2024
Added Mac & Linux Local Support.
### Update - May 3rd, 2024
Added Ipywidgets UI Kaggle Notebook.
### Update - May 1st, 2024
Added LocalTunnel Tunnel Option for UI Colab & Kaggle.
### Update - April 30th, 2024
Added Cloudfare tunnel to the WEB UI ui colab and merged [not-holar pull request](https://huggingface.co/spaces/Nick088/Stable_Diffusion_Finetuned_Minecraft_Skin_Generator/discussions/2) to make the image asset display pixelated like minecraft instead of blurry and with a checked background for the web ui
### Update - April 29th, 2024
Added Ngrok tunnel to the WEB UI Colab, added kaggle WEB & NO UI notebooks!
### Update - April 28th, 2024
Add a way to see the skin in 3d model preview and also download it for all versions thanks to:
- daroche (helping me fix the 3d model texture isue)
- [Brottweiler](https://gist.github.com/Brottweiler/483d0856c6692ef70cf90bf1a85ce364) (script to fix the 3d model texture
- [meew](https://huggingface.co/spaces/meeww/Minecraft_Skin_Generator/blob/main/models/player_model.glb) (Minecraft Player 3d model)
### Update - April 13th, 2024
Nick088 improved the local installation
### Update - April 12th, 2024
Nick088 made the Hugging Face Space and the Google Colab agradio Ui (based on the hf space)
### Update - April 11th, 2024
Nick088 Forked this repository and uploaded an updated version of the 2 py scripts with more features and uploaded the Google Colabs to run this model for free on the CPU (slower) or Free Daily Colab T4 Gpu
### 💥 Update - February 19th, 2024 💥
We have released a new open sourced Minecraft Skin Generator XL model based on Stable Diffusion XL. It offers many improvements over the original model, including support for the transparency layer.
The new model can be [downloaded from HuggingFace](https://huggingface.co/monadical-labs/minecraft-skin-generator-sdxl), or see below for commandline usage via the minecraft-skins-sdxl.py script.

## Credits
- Author of the AI Model: Cory Spencer <cory@monadical.com>
- Forked Improved Version: [Nick088](https://linktr.ee/Nick088)
- daroche (helping me fix the 3d model texture isue)
- [Brottweiler](https://gist.github.com/Brottweiler/483d0856c6692ef70cf90bf1a85ce364) (script to fix the 3d model texture)
- [not-holar](https://huggingface.co/not-holar) (made the rendering of the image asset in the web ui look pixelated like minecraft and have a checkered background)
- [meew](https://huggingface.co/spaces/meeww/Minecraft_Skin_Generator/blob/main/models/player_model.glb) (Minecraft Player 3d model)


