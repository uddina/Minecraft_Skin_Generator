# Stable Diffusion Minecraft Skin Generator

[![Discord](https://img.shields.io/discord/1198701940511617164?color=%23738ADB&label=Discord&style=for-the-badge)](https://discord.gg/dnrgs5GHfG)

## Overview

The process of fine tuning a Stable Diffusion model to generate Minecraft character previews is detailed here: [Digging into Stable Diffusion-Generated Minecraft Skins](https://monadical.com/posts/mincraft-skin-generation.html).

This codebase further refines that model, and allows for in-game skins to be generated using only a text prompt.  The finetuned model for doing so is available on HuggingFace as [monadical-labs/minecraft-skin-generator](https://huggingface.co/monadical-labs/minecraft-skin-generator).  The model development process is described here in a subsequant blog post: [Even More Skin in the Game: Digging Deeper Into Stable Diffusion-Generated Minecraft Skins](https://monadical.com/posts/minecraft-skins-part2.html).

## Example

Prompt: "A man in a purple suit wearing a tophat"

Output Image Asset Skin:

![images/purple.png](images/purple.png)

Skin Imported In Game:

![images/minecraft-screenshot.png](images/minecraft-screenshot.png)

# Usage

## Local

### Precompiled

1. Click the Code button and download it as a Zip.

2. Extract the .zip file.

3: Now you gotta Inference:

A: Choose UI or NO UI:

- UI: Open Run_Inference_UI.bat, let it create the venv_ui and install the requirements. After that ctrl+click the local url.

- NO UI: Open Run_Inference_NO_UI.bat, let it create the venv_no_ui and install the requirements.

B: Enter the prompt, so how the Minecraft Skins should look like.

C: Choose the Stable Diffusion Model, either 2 or xl (which is better).

D: Enter the integer value for the Inference Steps, which is basically denoising the image so an higher value = better output but longer process.

E: Enter the guidance scale, the float value for how much the output is adherent to the prompt.

F: Enter the model precision type,fp16 (which is faster) or fp32 (which is more precise but slower and need more resources).

G: Put the Seed, the starting point to initiate the generation process, either an integer value or 0 for a random one.

H: Write the Output Image Skin Asset Name with the .png extension.

I: Choose if to show a verbose (detailed) output or not, not really needed (y or n).

4. If you are running NO UI The output skin will be saved into the output_minecraft_skins folder with the output name you gave it before, else just download it by the download icon in the ui version in the web ui when its done making the skin.
5. You can import now the skin into Minecraft, which is slightly different way based on the version you play so just google it lol.

## Online

### Website
We have released a hosted version of our Minecraft Skin Generator at: [https://www.skingenerator.io](https://www.skingenerator.io)

While closed source, this version improves on the quality of generated skins from the publicly available model, plus it supports transparency in the helmet/hair section of the skins.  Please check it out and let us know what you think!

### Google Colab

#### NO UI
Run <a target="_blank" href="https://colab.research.google.com/github/Nick088Official/Stable_Diffusion_Finetuned_Minecraft_Skin_Generator/blob/main/Stable_Diffusion_Finetuned_Minecraft_Skin_Generator_NO_UI.ipynb">
  <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/>
</a>
#### UI

##### Ipywidgets
Run <a target="_blank" href="https://colab.research.google.com/github/Nick088Official/Stable_Diffusion_Finetuned_Minecraft_Skin_Generator/blob/main/Stable_Diffusion_Finetuned_Minecraft_Skin_Generator_Ipywidgets_UI.ipynb">
  <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/>
</a>

##### Gradio **(WARNING: COULD RISK YOUR FREE TIER COLAB ACC)**
Run <a target="_blank" href="https://colab.research.google.com/github/Nick088Official/Stable_Diffusion_Finetuned_Minecraft_Skin_Generator/blob/main/Stable_Diffusion_Finetuned_Minecraft_Skin_Generator_Gradio_UI.ipynb">
  <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/>
</a>

### Hugging Face Space
You can use the [Hugging Face Space](https://huggingface.co/spaces/Nick088/Stable_Diffusion_Finetuned_Minecraft_Skin_Generator), you can duplicate it by clicking the 3 dots in the right up corner and duplicate it on cpu to skip queue and also you can use your paid GPU to make it go faster


## Changelog
### Update - April 13th, 2024
Nick088 improved the local installation

### Update - April 12th, 2024
Nick088 made the Hugging Face Space and the Google Colab agradio Ui (based on the hf space)

### Update - April 11th, 2024
Nick088 Forked this repository and uploaded an updated version of the 2 py scripts with more features and uploaded the Google Colabs to run this model for free on the CPU (slower) or Free Daily Colab T4 Gpu!

### 💥 Update - February 19th, 2024 💥
We have released a new open sourced Minecraft Skin Generator XL model based on Stable Diffusion XL. It offers many improvements over the original model, including support for the transparency layer.

The new model can be [downloaded from HuggingFace](https://huggingface.co/monadical-labs/minecraft-skin-generator-sdxl), or see below for commandline usage via the minecraft-skins-sdxl.py script.

## Credits
Author of the AI Model: Cory Spencer <cory@monadical.com>

Forked Improved Version: [Nick088](https://linktr.ee/Nick088)
