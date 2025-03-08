import os
import tomli
import json
import subprocess


def compile_recipes(recipe_name):
    """Compile the recipes."""
    subprocess.run(["python", recipe_name])


def compile_project(project_name, zip_pack=False):
    """Compile the data pack."""
    print(f"[  0%] Compiling the data pack: {project_name}")
    
    # Check if the project exists
    if not os.path.exists(f"./{project_name}"):
        print(f"[100%] Project '{project_name}' does not exist.")
        return
    
    # Check the meta.toml file exists
    if not os.path.exists(f"./{project_name}/meta.toml"):
        print(f"[100%] Project '{project_name}' is missing a meta.toml file.")
        return
    
    # Read the meta.toml file
    print(f"[ 10%] Reading the meta.toml file")
    f_toml = open(f"./{project_name}/meta.toml", 'rb')
    meta = tomli.load(f_toml)
    f_toml.close()

    # Create the output directory
    print(f"[ 20%] Creating the output directory")
    output_dir = f"./datapacks/{meta['project']['name']}"
    if os.path.exists(output_dir):
        print(f"[100%] Error: Output directory '{output_dir}' already exists.")
        return
    os.makedirs(output_dir)

    # Create the pack.mcmeta file
    print(f"[ 30%] Creating the pack.mcmeta file")
    f_pack = open(f"{output_dir}/pack.mcmeta", 'w')
    mcmeta = {
        "pack": {
            "pack_format": 61,
            "supported_formats": 61, 
            "description": [
                {
                    "text": meta['project']['name'],
                    "color": "green"
                },{
                    "text": f" v{meta['project']['version']} by {meta['project']['author']}",
                    "color": "gray"
                },{
                    "text": f"\n{meta['project']['description']}",
                    "color": "white"
                }
            ]
        }
    }
    json.dump(mcmeta, f_pack, indent=4)
    f_pack.close()

    # create the data directory, and change the working directory to it
    os.makedirs(f"{output_dir}/data")
    proj_dir = os.path.join(os.getcwd(), f"./{project_name}")
    os.chdir(f"{output_dir}/data")
    work_dir = os.getcwd()

    # compile the recipes
    print(f"[ 40%] Compiling the recipes")
    if not os.path.exists(os.path.join(proj_dir, "recipes.py")):
        print(f"[ 45%] Project '{project_name}' is missing a recipes.py file.")
    else:
        compile_recipes(os.path.join(proj_dir, "recipes.py"))