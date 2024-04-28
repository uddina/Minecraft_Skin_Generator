import subprocess
import os
from PIL import Image, ImageEnhance
from pygltflib import GLTF2
from pygltflib.utils import ImageFormat, Texture, Material, Image as GLTFImage
import argparse

# Create an argument parser
parser = argparse.ArgumentParser(description='Fix texture generated minecraft skin from 64x32 to 64x64 to render it on the 3d model viewer')
parser.add_argument('filename_skin', type=str, help='Filename of the generated skin')
args = parser.parse_args()
filename_skin = args.filename_skin

os.chdir("..")

to3d_model_command = f"sh Scripts/64x32to64x64skin3dmodel.sh output_minecraft_skins/{filename_skin}"
    
os.system(to3d_model_command)
    
filename_3d_model = "Scripts/3d_model_player.glb"
gltf = GLTF2().load(filename_3d_model)

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
    new_image.uri = os.path.join(f"output_minecraft_skins/{filename}-converted.png")
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

    output_3d_model = f"{filename}_3d_model.glb"
    gltf.save(output_3d_model)
else:
    print("Invalid existing_texture_index")
