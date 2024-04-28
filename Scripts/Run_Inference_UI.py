import subprocess
import os
import gradio as gr
import torch

if torch.cuda.is_available():
    device = "cuda"
    print("Using GPU")
else:
    device = "cpu"
    print("Using CPU")
 

def run_inference(prompt, stable_diffusion_model, num_inference_steps, guidance_scale, model_precision_type, seed, output_image_name, verbose):
    if stable_diffusion_model == '2':
        sd_model = "minecraft-skins"
    else:
        sd_model = "minecraft-skins-sdxl"

    command = f"python Python_Scripts/{sd_model}.py '\"{prompt}\"' {num_inference_steps} {guidance_scale} {model_precision_type} {seed} {output_image_name} {'--verbose' if verbose else ''}"
    
    os.system(command)

    return os.path.join(f"output_minecraft_skins/{output_image_name}")

    
# Define Gradio UI components
prompt = gr.Textbox(label="Your Prompt", info="What the Minecraft Skin should look like")
stable_diffusion_model = gr.Dropdown(['2', 'xl'], value="xl", label="Stable Diffusion Model", info="Choose which Stable Diffusion Model to use, xl understands prompts better")
num_inference_steps = gr.Number(label="Number of Inference Steps", precision=0, value=25)
guidance_scale = gr.Number(minimum=0.1, value=7.5, label="Guidance Scale", info="The number of denoising steps of the image. More denoising steps usually lead to a higher quality image at the cost of slower inference")
model_precision_type = gr.Dropdown(["fp16", "fp32"], value="fp16", label="Model Precision Type", info="The precision type to load the model, like fp16 which is faster, or fp32 which gives better results")
seed = gr.Number(value=42, label="Seed", info="A starting point to initiate generation, put 0 for a random one")
output_image_name = gr.Textbox(label="Output Image Name", info="The name of the file of the output image skin, keep the .png", value="output-skin.png")
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
        output_image_name,
        verbose
    ],
    outputs=gr.Image(label="Generated Minecraft Skin Image Asset"),
    title="Minecraft Skin Generator",
    description="Make AI generated Minecraft Skins by a Finetuned Stable Diffusion Version!<br>Model used: https://github.com/Nick088Official/Stable_Diffusion_Finetuned_Minecraft_Skin_Generator<br>Hugging Face Space made by [Nick088](https://linktr.ee/Nick088)",
).launch(show_api=False, share=False)
