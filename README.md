# Texture List Generator For Minecraft Addons by TheDiamondBlue1
Helps you create the '_textures_list.json_' automatically!
## Overview
We have developed a Python script that generates a '_textures_list.json_' file within your textures folder. This tool is designed to save you time by automatically listing every texture path, eliminating the need to manually write each line. This is particularly beneficial for addons with numerous textures, like ours, which includes over 500 textures. We created this solution to streamline the process and are excited to share it with the community.

### Why do you need the '_textures_list.json_' file?
The '_textures_list.json_' file is crucial for Minecraft as it caches each texture, allowing for faster retrieval compared to scanning every image in your textures folder. This is particularly important when dealing with a large number of textures. Without this file, Minecraft might incorrectly load or even fail to load textures, potentially swapping them or causing errors. Additionally, Minecraft may generate a content log warning if textures are not listed in this file. While it can be overlooked for small texture sets, it is highly recommended to list all textures to ensure smooth operation.[^1]
## What you need/The Set-Up
### Prerequisites
1. Install Python

    Ensure Python is installed on your computer.
    - Download Python from the [official website](https://www.python.org/downloads/)
2. Access the Command Terminal
  
    Depending on your code editor, access the terminal:
    - **Visual Studio Code**: Click the **Terminal** tab at the top of the screen, the select **New Terminal**.
    - **Other Editors**: Open the **Start Menu** and search for "Command", then click **Command Prompt**.
3. Organise Your Textures

    Ensure you have a **Textures** folder:
    - Organise textures into the followinf subfolders:
      - '_blocks_'
      - '_entity_'
      - '_gui_'
      - '_items_'
      - '_misc_'
      - '_models_'
      - '_particle_'
      - '_ui_'
    - _Note_: If your create additional folder inside the textures folder, update the Python script accordingly.
4. Create the Python Script

    In your Addon folder, create a Python file.
   - Name it something like '_updated_textures.py_'.
5. Copy the Python Script

    Copy our Python script into your newly created file.
6. Set the Terminal Directory

     Ensure the terminal points to your addon's resource folder:
     - Navigate to your Addon's resource folder and copy the path.
     - Run the command: '***cd {Your Path}***'
       - Example: '***cd C:\Users\Admin\Documents***'
7. Run the Python Script

    Execute the script by typing: '***python updated_textures.py***'
    - The script will update your '_textures_list.json_' and respond with: **Updated textures\textures_list.json with the paths of the images without extensions, prefixed with 'textures/'.**
Simply run this command whenever you need to update your '_textures_list.json_'.
[^1]: This is from [Bedrock Wiki](https://wiki.bedrock.dev/concepts/textures-list.html)
