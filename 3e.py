import os
import argparse


def list_dirs(path, skip, only_dirs, level=0):
    if os.path.basename(path) in skip:
        return
    if only_dirs and not os.path.isdir(path):
        return
    try:
        print('  ' * level + '|-- ' + os.path.basename(path))
        if os.path.isdir(path):
            for item in os.listdir(path):
                list_dirs(os.path.join(path, item), skip, only_dirs, level + 1)
    except PermissionError:
        print('  ' * level + '|-- ' + os.path.basename(path) + ' (permission denied)')


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
    else:
        list_dirs(args.path, args.skip, args.only_dirs)


if __name__ == "__main__":
    main()
