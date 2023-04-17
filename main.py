import os
import re
import shutil

from tqdm import tqdm

def walk(path):
    remove_dirs = []
    non_grated_folders = [
        '__Previews',
        'History',
        'OldVersions',
        'Project Logs for *',
        'Free Documents Logs for *',
    ]
    compiled_matches = [re.compile(i) for i in non_grated_folders]
    print('Scanning...')
    for root, dirs, _ in tqdm(os.walk(path)):
        for dir in dirs:
            for valid in compiled_matches:
                if valid.match(dir):
                    remove_dirs.append(os.path.join(root, dir))
    return remove_dirs


def main():
    dirs = walk('.')
    print('Dirs to remove:')
    for dir in dirs:
        print(dir)
    while True:
        print('Delete. Are you sure? [y/n]')
        answer = input().lower()
        if answer == 'y':
            print('Deleting dirs...')
            for dir in tqdm(dirs):
                shutil.rmtree(dir)
            print('Done!')
            input()
            exit(0)
        if answer == 'n':
            print('Nothing to do. Exiting...')
            exit(0)
        else:
            print('Wrong answer, try again.')
            continue
    


if __name__ == '__main__':
    main()