import os
import json

# Define the directory containing the textures folders
textures_directory = 'textures'

# List of folders to scan for images
folders = ["blocks", "entity", "gui", "items", "misc", "models", "particle", "ui",]

# Define the path to the JSON file
json_file_path = os.path.join(textures_directory, "textures_list.json")

# Function to scan folders and collect image paths
def collect_image_paths(base_dir, folders):
    image_paths = []
    for folder in folders:
        folder_path = os.path.join(base_dir, folder)
        for root, _, files in os.walk(folder_path):
            for file in files:
                if file.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
                    relative_path = os.path.relpath(os.path.join(root, file), base_dir).replace('\\', '/')
                    path_without_extension = os.path.splitext(relative_path)[0]
                    prefixed_path = f"textures/{path_without_extension}"
                    image_paths.append(prefixed_path)
    return image_paths

# Function to update the JSON file
def update_json_file(json_file_path, image_paths):
    with open(json_file_path, 'w') as json_file:
        json.dump(image_paths, json_file, indent=4)

# Collect image paths
image_paths = collect_image_paths(textures_directory, folders)

# Update the JSON file
update_json_file(json_file_path, image_paths)

print(f"Updated {json_file_path} with the paths of the images without extensions, & prefixed with 'textures/'.")