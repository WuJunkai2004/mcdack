import argparse

# define arguments parser
parser = argparse.ArgumentParser(description='MCDACK: A tool for creating and compiling Minecraft data packs.')

# add subparsers for commands
subparsers = parser.add_subparsers(dest='command')

# create command
create_parser = subparsers.add_parser('create', help='Create a new data pack template')
create_parser.add_argument('project_name', type=str, help='Name of the new project')

# compile command
compile_parser = subparsers.add_parser('compile', help='Compile the data pack')
compile_parser.add_argument('project_name', type=str, help='Name of the project to compile')
compile_parser.add_argument('-z', '--zip', action='store_true', help='Zip the compiled data pack')

# parse arguments
args = parser.parse_args()

# handle commands
if args.command == 'create':
    # handle create command
    print(f"Creating a new data pack template: {args.project_name}")
    # ...existing code for creating a template...
elif args.command == 'compile':
    # handle compile command
    print(f"Compiling the data pack: {args.project_name}")
    if args.zip:
        print("Zipping the compiled data pack")
    # ...existing code for compiling the data pack...
else:
    parser.print_help()