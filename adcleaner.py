import argparse
import os
import re
import sys
import shutil

from tqdm import tqdm


def init_argparse():
    parser = argparse.ArgumentParser(description='Altium Designer & Autodesk Inventor cleaner')
    parser.add_argument('-p', '--path', type=str, help='Path to scan for files. Scans from "." if not specified')
    return parser.parse_args()


def walk(path):
    remove_dirs = []
    remove_files = []
    non_grated_folders = [
        '__Previews',
        'History',
        'OldVersions',
        'Project Logs for *',
        'Free Documents Logs for *',
    ]
    non_grated_files = [
        'Thumbs.db'
    ]
    compiled_dir_matches = [re.compile(i) for i in non_grated_folders]
    compiled_file_matches = [re.compile(i) for i in non_grated_files]
    print('Scanning...')
    for root, dirs, files in tqdm(os.walk(path)):
        for file in files:
            for valid in compiled_file_matches:
                if valid.match(file):
                    remove_files.append(os.path.join(root, file))
        for dir in dirs:
            for valid in compiled_dir_matches:
                if valid.match(dir):
                    remove_dirs.append(os.path.join(root, dir))
    return remove_dirs, remove_files


def main():
    args = init_argparse()
    if args.path:
        path = args.path
    else:
        path = '.'
    dirs, files = walk(path)
    if not dirs and not files:
        print('Nothing to delete. Press any key to exit..')
        input()
        exit(0)
    print('files and dir to remove:')
    for dir in dirs:
        print(f'[Dir] {dir}')
    for file in files:
        print(f'[File] {file}')
    while True:
        print('Delete? Are you sure? [y/n]')
        answer = input().lower()
        if answer == 'y':
            print('Deleting directories...')
            for dir in tqdm(dirs):
                try:
                    shutil.rmtree(dir)
                    tqdm.write(f'Deleted {dir}')
                except OSError:
                    tqdm.write(f'Can\'t delete {dir}', file=sys.stderr)
            print('Done!')
            print('Deleting files...')
            for file in tqdm(files):
                try:
                    os.remove(file)
                    tqdm.write(f'Deleted {file}')
                except OSError:
                    tqdm.write(f'Can\'t delete {file}', file=sys.stderr)
            print('Done! Press any key to exit...')
            input()
            exit(0)
        if answer == 'n':
            print('Nothing to do. Press any key to exit...')
            input()
            exit(0)
        else:
            print('Wrong answer, try again.')
            continue


if __name__ == '__main__':
    main()