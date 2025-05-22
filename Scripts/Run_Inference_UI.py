import subprocess
import os
import gradio as gr
import torch
import numpy as np
from PIL import Image, ImageEnhance
from argparse import ArgumentParser


# cli arguments
if __name__ == "__main__":
    parser = ArgumentParser(
       description="Generate Minecraft Skins with Stable Diffusion Finetuned Models",
       epilog="Example: python app.py --share --listen-port 0088 --open"
    )
    parser.add_argument(
       "--share",
       action="store_true",
       help="Enable sharing of the interface through Gradio's temporary Public URLs"
    )
    parser.add_argument(
       "--listen-port",
       type=int,
       default=7860,
       help="The listening port that the server will use (default: 7860)"
    )
    parser.add_argument(
       "--open",
       action="store_true",
       help="Automatically open the interface in the default web browser"
    )   
    args = parser.parse_args()


MAX_SEED = np.iinfo(np.int32).max


def run_inference(prompt, stable_diffusion_model, num_inference_steps, guidance_scale, model_precision_type, seed, filename, verbose, see_in_3d):

    # inference
    if stable_diffusion_model == '2':
        sd_model = "minecraft-skins"
    else:
        sd_model = "minecraft-skins-sdxl"

    inference_command = f"python Scripts/{sd_model}.py '{prompt}' {num_inference_steps} {guidance_scale} {model_precision_type} {seed} {filename} {'--verbose' if verbose else ''}"
    
    os.system(inference_command)

    # view it in 3d or not
    if see_in_3d:
        from pygltflib import GLTF2
        from pygltflib.utils import ImageFormat, Texture, Material, Image as GLTFImage
        os.chdir("Scripts")
        command_3d_model = f"python to_3d_model.py '{filename}'"
        os.system(command_3d_model)
        os.chdir("..")
        glb_path = os.path.join(f"output_minecraft_skins/{filename}_3d_model.glb")
        return os.path.join(f"output_minecraft_skins/{filename}"), (f"output_minecraft_skins/{filename}-converted.png"), glb_path
    else:
        return os.path.join(f"output_minecraft_skins/{filename}"), (f"output_minecraft_skins/{filename}-converted.png"), None


# Define Gradio UI components
prompt = gr.Textbox(label="Your Prompt", info="What the Minecraft Skin should look like")
stable_diffusion_model = gr.Dropdown(['2', 'xl'], value="xl", label="Stable Diffusion Model", info="Choose which Stable Diffusion Model to use, xl understands prompts better")
num_inference_steps = gr.Slider(label="Number of Inference Steps", info="The number of denoising steps of the image. More denoising steps usually lead to a higher quality image at the cost of slower inference", minimum=1, maximum=50, value=25, step=1)
guidance_scale = gr.Slider(label="Guidance Scale", info="Controls how much the image generation process follows the text prompt. Higher values make the image stick more closely to the input text.", minimum=0.0, maximum=10.0, value=7.5, step=0.1)
model_precision_type = gr.Dropdown(["fp16", "fp32"], value="fp16", label="Model Precision Type", info="The precision type to load the model, like fp16 which is faster, or fp32 which is more precise but more resource consuming")
seed = gr.Slider(value=42, minimum=0, maximum=MAX_SEED, step=1, label="Seed", info="A starting point to initiate the generation process, put 0 for a random one")
filename = gr.Textbox(label="Output Image Name", info="The name of the file of the output image skin, keep the.png", value="output-skin.png")
see_in_3d = gr.Checkbox(label="See in 3D", info="View the generated skin as a 3D Model", value=True)
verbose = gr.Checkbox(label="Verbose Output", info="Produce more detailed output while running", value=False)


# Create the Gradio interface
gr.Interface(
    fn=run_inference,
    inputs=[
        prompt,
        stable_diffusion_model,
        num_inference_steps,
        guidance_scale,
        model_precision_type,
        seed,
        filename,
        see_in_3d,
        verbose
    ],
    outputs=[
        gr.Image(label="Generated Minecraft Skin Image Asset", elem_classes="pixelated checkered"),
        gr.Image(label="Converted PNG"),
        gr.Model3D(clear_color=[0.0, 0.0, 0.0, 0.0],  label="3D Model")
    ],
    title="Minecraft Skin Generator",
    description="Make AI generated Minecraft Skins by a Finetuned Stable Diffusion Version!<br>Github Repository & Model used: https://github.com/Nick088Official/Minecraft_Skin_Generator<br>Credits: [Monadical-SAS](https://github.com/Monadical-SAS/minecraft_skin_generator) (Creators of the model), [Nick088](https://linktr.ee/Nick088) (Improving usage of the model), daroche (helping me fix the 3d model texture isue), [Brottweiler](https://gist.github.com/Brottweiler/483d0856c6692ef70cf90bf1a85ce364)(script to fix the 3d model texture, [meew](https://huggingface.co/spaces/meeww/Minecraft_Skin_Generator/blob/main/models/player_model.glb) (Minecraft Player 3d model)",
    css=".pixelated {image-rendering: pixelated} .checkered img {background-image: url(\'data:image/svg+xml,<svg xmlns=\"http://www.w3.org/2000/svg\" width=\"2\" height=\"2\" fill-opacity=\".15\"><rect x=\"1\" width=\"1\" height=\"1\"/><rect y=\"1\" width=\"1\" height=\"1\"/></svg>\');background-size: 16px;}"
).launch(
    share=args.share,
    favicon_path="favicon.ico",
    server_port=args.listen_port,
    inbrowser=args.open
)
