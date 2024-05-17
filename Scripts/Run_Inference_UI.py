import subprocess
import os
import gradio as gr
import torch
from PIL import Image, ImageEnhance
import spaces


if torch.cuda.is_available():
    device = "cuda"
    print("Using GPU")
else:
    device = "cpu"
    print("Using CPU")


subprocess.run(["git", "clone", "https://github.com/Nick088Official/Stable_Diffusion_Finetuned_Minecraft_Skin_Generator.git"])

os.chdir("Stable_Diffusion_Finetuned_Minecraft_Skin_Generator")


@spaces.GPU()
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
        return os.path.join(f"output_minecraft_skins/{filename}"), glb_path
    else:
        return os.path.join(f"output_minecraft_skins/{filename}"), None


# Define Gradio UI components
prompt = gr.Textbox(label="Your Prompt", info="What the Minecraft Skin should look like")
stable_diffusion_model = gr.Dropdown(['2', 'xl'], value="xl", label="Stable Diffusion Model", info="Choose which Stable Diffusion Model to use, xl understands prompts better")
num_inference_steps = gr.Number(label="Number of Inference Steps", precision=0, value=25)
guidance_scale = gr.Number(minimum=0.1, value=7.5, label="Guidance Scale", info="The number of denoising steps of the image. More denoising steps usually lead to a higher quality image at the cost of slower inference")
model_precision_type = gr.Dropdown(["fp16", "fp32"], value="fp16", label="Model Precision Type", info="The precision type to load the model, like fp16 which is faster, or fp32 which is more precise but more resource consuming")
seed = gr.Number(value=42, label="Seed", info="A starting point to initiate generation, put 0 for a random one")
filename = gr.Textbox(label="Output Image Name", info="The name of the file of the output image skin, keep the.png", value="output-skin.png")
see_in_3d = gr.Checkbox(label="See in 3D", info="View the generated skin as a £D Model", value=True)
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
        gr.Model3D(clear_color=[0.0, 0.0, 0.0, 0.0],  label="3D Model")
    ],
    title="Minecraft Skin Generator",
    description="Make AI generated Minecraft Skins by a Finetuned Stable Diffusion Version!<br>Model used: https://github.com/Nick088Official/Stable_Diffusion_Finetuned_Minecraft_Skin_Generator<br>Credits: [Monadical-SAS](https://github.com/Monadical-SAS/minecraft_skin_generator) (Creators of the model), [Nick088](https://linktr.ee/Nick088) (Improving usage of the model), daroche (helping me fix the 3d model texture isue), [Brottweiler](https://gist.github.com/Brottweiler/483d0856c6692ef70cf90bf1a85ce364)(script to fix the 3d model texture, [meew](https://huggingface.co/spaces/meeww/Minecraft_Skin_Generator/blob/main/models/player_model.glb) (Minecraft Player 3d model)",
    css=".pixelated {image-rendering: pixelated} .checkered img {background-image: url(\'data:image/svg+xml,<svg xmlns=\"http://www.w3.org/2000/svg\" width=\"2\" height=\"2\" fill-opacity=\".15\"><rect x=\"1\" width=\"1\" height=\"1\"/><rect y=\"1\" width=\"1\" height=\"1\"/></svg>\');background-size: 16px;}"
).launch(show_api=False, share=False)
