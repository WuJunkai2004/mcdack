import argparse

from mcdack.create    import create_project
from mcdack.compile   import compile_project

# define arguments parser
parser = argparse.ArgumentParser(
    description='MCDACK: A tool for creating and compiling Minecraft data packs.',
    prog='python -m mcdack'
)


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




if args.command == 'create':
    create_project(args.project_name)
elif args.command == 'compile':
    compile_project(args.project_name, args.zip)
else:
    parser.print_help()