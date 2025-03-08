import os

def create_project(project_name):
    """Create a new data pack template."""
    dir_path = os.path.join(os.getcwd(), project_name)
    
    # check the project directory does not already exist
    # if it does, raise an error
    if os.path.exists(dir_path):
        print(f"Error: Project directory '{project_name}' already exists.")
        return
    
    # create the project directory
    os.makedirs(dir_path)

    # create the data pack rawdata directory
    os.makedirs(os.path.join(dir_path, 'rawdata'))

    # write the files
    #├─ recipes.py
    #├─ functions.py
    #├─ loot_tables.py
    #├─ advancements.py
    #├─ flipflops.py
    created_files = [ 'recipes.py', 'functions.py', 'loot_tables.py', 'advancements.py', 'flipflops.py', 'meta.toml' ]
    files_head = {
        'recipes.py': '''
from mcdack.recipe import *
from mcdack.metadata import *
''',
        'meta.toml': '''
[project]
name = "My Project"
description = "A description of the project"
version = "1.0.0"
author = "Author Name"
'''
    }    
    for file in created_files:
        with open(os.path.join(dir_path, file), 'w') as f:
            f.write(f"# {file}\n\n")
            f.write(files_head.get(file, ''))

    toml_model = '''
[project]
name = {}
description = {}
author = {}'''
    project_name = project_name.replace(' ', '_')
    description = input("Enter a description: ")
    author = input("Enter the author's name: ")
    with open(os.path.join(dir_path, 'meta.toml'), 'w') as f:
        f.write(toml_model.format(project_name, description, author))
