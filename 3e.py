import os
import argparse


def list_dirs(path, skip, only_dirs, level=0, prefix=''):
    try:
        if os.path.basename(path) in skip:
            return
        if only_dirs and not os.path.isdir(path):
            return
        is_dir = os.path.isdir(path)
        items = os.listdir(path) if is_dir else []
        items = [item for item in items if not (os.path.isfile(os.path.join(path, item)) and only_dirs)]
        if level == 0:
            print(os.path.basename(path))
        for i, item in enumerate(items):
            is_last = i == len(items) - 1
            new_prefix = prefix + ('└───' if is_last else '├───')
            print(new_prefix + os.path.basename(item))
            next_prefix = prefix + ('    ' if is_last else '│   ')
            list_dirs(os.path.join(path, item), skip, only_dirs, level + 1, next_prefix)
    except PermissionError:
        print(prefix + '├───' + os.path.basename(path) + ' (permission denied)')


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
 \\______/  \\_______|(tree)
    a better tree command for windows.
    by @tzero86
'''
    )


def main():
    try:
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
        elif args.path in ['/', '\\']:
            args.path = os.path.abspath(os.sep)  # replace '/' or '\\' with the absolute path of the root directory

        list_dirs(args.path, args.skip, args.only_dirs)
    except KeyboardInterrupt:
        print(f"\n Interrupted by user. Exiting...")
        banner()


if __name__ == "__main__":
    main()
