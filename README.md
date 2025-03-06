# mcdack

Write minecraft data pack like a python script


## Installation

```bash
pip install mcdack
```

## Usage
### Create a new data pack template
```bash
python -m mcdack create <project_name>
```
then you will get a new mcdack template project filefolder, which can be compiled to a minecraft data pack.

It will have the following files and folders:
```
<project_name>
├── rawdata (folder for raw data)
├─ recipe.py
├─ function.py
├─ loot_table.py
├─ advancement.py
├─ flipflop.py
├─ README.md
```

Then you can write your data pack in the python script files.


### Compile the data pack
```bash
python -m mcdack compile <project_name>
```
Then you will get a compiled data pack folder titled `<project_name>`.
or you can zip the compiled folder by
```bash
python -m mcdack compile <project_name> -z
```
Then you will get a compiled data pack zip file titled `<project_name>.zip`.


### Write data pack like a python script
()[./example.py]