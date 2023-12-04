import os
import sys
from subprocess import PIPE, run
import shutil
import json

PATTERN = "dite"


def find_dite_dirs(source_path):
    dirs = os.listdir(source_path)
    dite_paths = []
    for root, dirs, files in os.walk(source_path):
        for directory in dirs:
            if PATTERN in directory:
                path = os.path.join(source_path, directory)
                dite_paths.append(path)
    return dite_paths


def create_dir(path):
    if not os.path.exists(path):
        os.mkdir(path)


def get_name_from_path(paths, to_replace):
    new_paths = []
    for path in paths:
        _, name = os.path.split(path)
        name = name.replace(to_replace, "")
        new_paths.append(name)
    return new_paths


def main(source, target):
    cwd = os.getcwd()
    # Create corresponding file paths
    source_path = os.path.join(cwd, source)
    target_path = os.path.join(cwd, source)

    # Find all dite files
    dite_dirs = find_dite_dirs(source_path)
    new_dite_dirs = get_name_from_path(dite_dirs, "-dite")
    print(new_dite_dirs)

    create_dir(target_path)


if __name__ == '__main__':
    args = sys.argv
    if len(args) != 3:
        raise Exception(
            "Usage: python3 folder-dite-copy <source-folder> <target-folder>")
    source, target = args[1:]
    main(source, target)
