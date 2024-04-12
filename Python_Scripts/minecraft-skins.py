import accelerate
import diffusers
from diffusers import StableDiffusionPipeline
from PIL import Image
import os
import random

import numpy as np
import argparse
import logging
import torch
import sys

MODEL_NAME = "monadical-labs/minecraft-skin-generator"
MASK_IMAGE = "images/skin-half-mask.png"

SCALE = 12

def extract_minecraft_skin(generated_image):
    # Extract the skin portion from the top half of the image.
    width, height = generated_image.size
    generated_skin = generated_image.crop((0, 0, width, height/2))
    
    # Scale the skin down to the expected size of 64x32 pixels.
    width, height = generated_skin.size
    scaled_skin = generated_skin.resize((int(width / SCALE), int(height / SCALE)), resample=Image.NEAREST) 
    
    return scaled_skin

def restore_skin_alphachannels(image):
    # Convert the image to RGBA.
    converted_image = image.convert('RGBA')

    # Convert the image into a numpy array.
    image_data = np.array(converted_image)
    red, green, blue, alpha = image_data.T

    # Convert all of the black pixels in the skin to slightly-less-black.
    # We're going to later use (0,0,0) as our transparency color, so this
    # will prevent transparent pixels in our skin.
    black_areas = (red == 0) & (blue == 0) & (green == 0)
    image_data[..., :-1][black_areas.T] = (1, 1, 1)

    # Convert the data back into Image format.
    converted_image = Image.fromarray(image_data)
    converted_image = converted_image.convert("P")

    # Enable transparency in the skin image.                                                                                                                                               
    converted_image = converted_image.convert("P")
    converted_image.info["transparency"] = 0
    converted_image = converted_image.convert("RGBA")
    
    # Load an imagemask of unused skin areas that shoudl be fully transparent.                                                                                          
    mask_image = Image.open(MASK_IMAGE)
    mask_image = mask_image.convert("RGBA")
    
    # Perform the alpha composite, and return the result.                                                                                                                             
    mask_image.alpha_composite(converted_image)
    
    return converted_image

def main(prompt, num_inference_steps, guidance_scale, num_images_per_prompt, model_precision_type, seed, filename, logger):
    # Enable GPU acceleration frameworks, if enabled.

    if model_precision_type == "fp16":
        dtype = torch.float16
    elif model_precision_type == "fp32":
        dtype = torch.float32

    if torch.cuda.is_available() and torch.backends.cuda.is_built():
        # A CUDA compatible GPU was found.
        logger.info("CUDA device found, enabling.")
        device = "cuda"
    elif torch.backends.mps.is_available() and torch.backends.mps.is_built():
        # Apple M1/M2 machines have the MPS framework.
        logger.info("Apple MPS device found, enabling.")
        device = "mps"
    else:
        # Else we're defaulting to CPU.
        device = "cpu"
        logger.info("No CUDA or MPS devices found, running on CPU.")

    # Load (and possibly download) our Minecraft model.
    logger.info("Loading HuggingFace model: '{}'.".format(MODEL_NAME))
    if device == "cpu":
        pipeline = StableDiffusionPipeline.from_pretrained(MODEL_NAME)
    else:
        pipeline = StableDiffusionPipeline.from_pretrained(MODEL_NAME, torch_dtype=dtype)
    pipeline.to(device)
    
    
    # random option for 0 seed
    if seed == 0:
        seed = random.randint(1, 100000)
    else:
        seed = seed


    # Generate the image given the prompt provided on the command line.
    logger.info("Generating skin with prompt: '{}'.".format(prompt))
    generated_image = pipeline(
        prompt=prompt,
        num_inference_steps=num_inference_steps,
        height=768,
        width=768,
        guidance_scale=guidance_scale,
        num_images_per_prompt=num_images_per_prompt,
        seed=seed
    ).images[0]

    # Extract and scale down the Minecraft skin portion of the image.
    logger.info("Extracting and scaling Minecraft skin from generated image.")
    minecraft_skin = extract_minecraft_skin(generated_image)

    logger.info("Restoring transparency in generated skin file.")
    # Clean up any background noise in the skin and restore the alphachannel transparency.
    minecraft_skin = restore_skin_alphachannels(minecraft_skin)

    logger.info("Saving skin to: '{}'.".format(filename))
    os.chdir("output_minecraft_skins")
    minecraft_skin.save(filename)
    os.chdir("..")
    
if __name__ == "__main__":
    logging.basicConfig(stream=sys.stdout, level=logging.ERROR, format='[%(asctime)s] %(levelname)s - %(message)s')

    logger = logging.getLogger("minecraft-skins")

    # Get all of the command line parameters and options passed to us.
    parser = argparse.ArgumentParser(description='Process the command line arguments.')

    parser.add_argument('prompt', type=str, help='Stable Diffusion prompt to be used to generate skin')
    parser.add_argument('num_inference_steps', type=int, help='The number of denoising steps of the image. More denoising steps usually lead to a higher quality image at the cost of slower inference')
    parser.add_argument('guidance_scale', type=float, help='How closely the generated image adheres to the prompt')
    parser.add_argument('num_images_per_prompt', type=int, help='The number of images to make with the prompt')
    parser.add_argument('model_precision_type', type=str, help='The precision type to load the model, like fp16 which is faster, or fp32 which gives better results')
    parser.add_argument('seed', type=int, help='A starting point to initiate the generation process, put 0 for random')
    parser.add_argument('filename', type=str, help='Name of the output generated Minecraft skin file')
    parser.add_argument('--verbose', help='Produce verbose output while running', action='store_true', default=False)

    args = parser.parse_args()

    filename = args.filename
    verbose = args.verbose
    prompt = args.prompt
    num_inference_steps = args.num_inference_steps
    guidance_scale = args.guidance_scale
    num_images_per_prompt = args.num_images_per_prompt
    model_precision_type = args.model_precision_type
    seed = args.seed
    
    if verbose:
        logger.setLevel(logging.INFO)
    
    main(prompt, num_inference_steps, guidance_scale, num_images_per_prompt, model_precision_type, seed, filename, logger)
    
