import os
import argparse


def list_dirs(path, skip, only_dirs, level=0, prefix=''):
    if os.path.basename(path) in skip:
        return
    if only_dirs and not os.path.isdir(path):
        return
    try:
        is_dir = os.path.isdir(path)
        items = os.listdir(path) if is_dir else []
        items = [item for item in items if not (os.path.isfile(os.path.join(path, item)) and only_dirs)]
        print(prefix + '├──' + os.path.basename(path))
        prefix += '    ' if prefix.endswith('└──') else '│   '
        for i, item in enumerate(items):
            new_prefix = prefix + '└──' if i == len(items) - 1 else prefix + '├──'
            list_dirs(os.path.join(path, item), skip, only_dirs, level + 1, new_prefix)
    except PermissionError:
        print(prefix + '├──' + os.path.basename(path) + ' (permission denied)')


def banner():
    print(
        '''
 $$$$$$\\            
$$ ___$$\\           
\\_/   $$ | $$$$$$\\  
  $$$$$ / $$  __$$\\ 
  \\___$$\\ $$$$$$$$ |
$$\\   $$ |$$   ____|
\\$$$$$$  |\\$$$$$$$\\ 
 \\______/  \\_______|
    a better tree command for windows.
    by @tzero86
'''
    )


def main():
    parser = argparse.ArgumentParser(
        description='Generate an ASCII tree representation of the directories on a given path.')
    parser.add_argument('path', type=str, nargs='?', default=None, help='The root path to generate the tree from.')
    parser.add_argument('--skip', nargs='+', default=[], help='Directories to skip.')
    parser.add_argument('--only-dirs', action='store_true', help='Only include directories in the tree.')
    args = parser.parse_args()

    if args.path is None:
        banner()
        parser.print_help()
        return
    elif args.path == '.':
        args.path = os.getcwd()  # replace '.' with the actual directory name

    list_dirs(args.path, args.skip, args.only_dirs)



if __name__ == "__main__":
    main()
