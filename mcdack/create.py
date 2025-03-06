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
    #├─ recipe.py
    #├─ function.py
    #├─ loot_table.py
    #├─ advancement.py
    #├─ flipflop.py
    created_files = [ 'recipe.py', 'function.py', 'loot_table.py', 'advancement.py', 'flipflop.py' ]
    for file in created_files:
        with open(os.path.join(dir_path, file), 'w') as f:
            f.write(f"# {file}\n\n")
    

