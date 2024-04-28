import subprocess
import os
import gradio as gr
import torch
from PIL import Image, ImageEnhance
from pygltflib import GLTF2
from pygltflib.utils import ImageFormat, Texture, Material, Image as GLTFImage


if torch.cuda.is_available():
    device = "cuda"
    print("Using GPU")
else:
    device = "cpu"
    print("Using CPU")


def run_inference(prompt, stable_diffusion_model, num_inference_steps, guidance_scale, model_precision_type, seed, output_image_name, verbose):

    os.chdir("Stable_Diffusion_Finetuned_Minecraft_Skin_Generator")
    
    if stable_diffusion_model == '2':
        sd_model = "minecraft-skins"
    else:
        sd_model = "minecraft-skins-sdxl"

    inference_command = f"python Scripts/{sd_model}.py '{prompt}' {num_inference_steps} {guidance_scale} {model_precision_type} {seed} {output_image_name} {'--verbose' if verbose else ''}"
    
    os.system(inference_command)
    
    os.chdir("..")
    
    to3d_model_command = f"sh 64x32to64x64skin3dmodel.sh Stable_Diffusion_Finetuned_Minecraft_Skin_Generator/output_minecraft_skins/{output_image_name}"
    
    os.system(to3d_model_command)

    
    filename = "3d_model_player.glb"
    gltf = GLTF2().load(filename)

    # Step 1: Find the index of the existing texture you want to replace
    # Let's assume the texture you want to replace is at index 1 (you need to replace 1 with the actual index)
    existing_texture_index = 0

    # Check if the existing_texture_index is valid
    if existing_texture_index < len(gltf.textures):
        # Step 2: Remove the old texture and its associated image from the GLB
        # Remove the texture
        gltf.textures.pop(existing_texture_index)

        # Remove the image associated with the texture
        existing_image_index = gltf.materials[0].pbrMetallicRoughness.baseColorTexture.index
        gltf.images.pop(existing_image_index)


        # Step 3: Add the new image and texture to the GLB
        # Create and add a new image to the glTF (same as before)
        new_image = GLTFImage()
        new_image.uri = os.path.join(f"Stable_Diffusion_Finetuned_Minecraft_Skin_Generator/output_minecraft_skins/{output_image_name}-converted.png")
        gltf.images.append(new_image)



        # Create a new texture and associate it with the added image
        new_texture = Texture()
        new_texture.source = len(gltf.images) - 1  # Index of the newly added image
        new_texture.sampler = 0
        # set to nearest neighbor

        gltf.textures.append(new_texture)

        # Step 4: Assign the new texture to the appropriate material(s) or mesh(es)
        # Assuming you have a mesh/primitive that was using the old texture and you want to apply the new texture to it, you need to set the material index for that mesh/primitive.
        # Replace 0 with the actual index of the mesh/primitive you want to update.
        gltf.materials[0].pbrMetallicRoughness.baseColorTexture.index = len(gltf.textures) - 1


        # Now you can convert the images to data URIs and save the updated GLB
        gltf.convert_images(ImageFormat.DATAURI)

        output_3d_model = "output_3d_model.glb"
        gltf.save(output_3d_model)
    else:
        print("Invalid existing_texture_index")


    # Return the generated image and the processed model
    return os.path.join(f"Stable_Diffusion_Finetuned_Minecraft_Skin_Generator/output_minecraft_skins/{output_image_name}"), output_3d_model

    
    
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
    outputs=[
        gr.Image(label="Generated Minecraft Skin Image Asset"),
        gr.Model3D(clear_color=[0.0, 0.0, 0.0, 0.0],  label="3D Model")
    ],
    title="Minecraft Skin Generator",
    description="Make AI generated Minecraft Skins by a Finetuned Stable Diffusion Version!<br>Model used: https://github.com/Nick088Official/Stable_Diffusion_Finetuned_Minecraft_Skin_Generator<br>Credits: [Monadical-SAS](https://github.com/Monadical-SAS/minecraft_skin_generator) (Creators of the model), [Nick088](https://linktr.ee/Nick088) (Improving usage of the model), daroche (helping me fix the 3d model texture isue), [Brottweiler](https://gist.github.com/Brottweiler/483d0856c6692ef70cf90bf1a85ce364) (script to fix the 3d model texture, [meew](https://huggingface.co/spaces/meeww/Minecraft_Skin_Generator/blob/main/models/player_model.glb) (Minecraft Player 3d model)",
).launch(show_api=False, share=False)
