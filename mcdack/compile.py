import os

def compile_project(project_name, zip_pack=False):
    """Compile the data pack."""
    print(f"Compiling the data pack: {project_name}")
    if zip_pack:
        print("Zipping the compiled data pack")
    # ...existing code for compiling the data pack...