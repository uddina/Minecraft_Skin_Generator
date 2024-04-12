# Stable Diffusion Minecraft Skin Generator

## Overview

The process of fine tuning a Stable Diffusion model to generate Minecraft character previews is detailed here: [Digging into Stable Diffusion-Generated Minecraft Skins](https://monadical.com/posts/mincraft-skin-generation.html).

This codebase further refines that model, and allows for in-game skins to be generated using only a text prompt.  The finetuned model for doing so is available on HuggingFace as [monadical-labs/minecraft-skin-generator](https://huggingface.co/monadical-labs/minecraft-skin-generator).  The model development process is described here in a subsequant blog post: [Even More Skin in the Game: Digging Deeper Into Stable Diffusion-Generated Minecraft Skins](https://monadical.com/posts/minecraft-skins-part2.html).

# Usage

## Local

1. Clone the minecraft\_skin\_generator GitHub repository onto your computer:

  ```python
  $ git clone https://github.com/Nick088Official/Stable_Diffusion_Finetuned_Minecraft_Skin_Generator.git
  $ cd Stable_Diffusion_Finetuned_Minecraft_Skin_Generator
  ```

2: Install requirements:

  ```python
  $ pip install -r requirements.txt
  ```

2. Skins can be generated using the Stable Diffusion 2 minecraft-skins.py script in the bin directory:

  ```python
  $ python /minecraft-skins.py output-skin.png "A man in a purple suit wearing a tophat"
  ```
To use the newer Stable Diffusion XL model, use the minecraft-skins-sdxl.py script:

  ```python
  $ python bin/minecraft-skins-sdxl.py output-skin.png "A man in a purple suit wearing a tophat"
  ```

4. The output skin will be saved into "output-skin.png" and should be similar to this:

  ![images/purple.png](images/purple.png)
  
5. The skin can then be imported directly into Minecraft:

  ![images/minecraft-screenshot.png](images/minecraft-screenshot.png)

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
You can use the [Hugging Face Space](https://huggingface.co/spaces/Nick088/Stable_Diffusion_Finetuned_Minecraft_Skin_Generator) which runs on CPU and will be slower, you can duplicate it by clicking the 3 dots in the right up corner and duplicate it on cpu to skip queue and also you can use your paid GPU to make it go faster


## Changelog
### Update - April 12th, 2024
Nick088 made the Hugging Face Space and the Google Colab agradio Ui (based on the hf space)

### Update - April 11th, 2024
Nick088 Forked this repository and uploaded an updated version of the 2 py scripts with more features and uploaded the Google Colabs to run this model for free on the CPU (slower) or Free Daily Colab T4 Gpu!

### 💥 Update - February 19th, 2024 💥

We have released a new open sourced Minecraft Skin Generator XL model based on Stable Diffusion XL. It offers many improvements over the original model, including support for the transparency layer.

The new model can be [downloaded from HuggingFace](https://huggingface.co/monadical-labs/minecraft-skin-generator-sdxl), or see below for commandline usage via the minecraft-skins-sdxl.py script.

## Author of the Original Model

Cory Spencer <cory@monadical.com>
