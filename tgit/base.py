import os
from . import data

def write_tree(directory='.'):
    with os.scandir(directory) as it:
        for entry in it:
            full_path = os.path.join(directory, entry.name)
            if is_ignored(full_path):
                continue
            if entry.is_file(follow_symlinks=False):
                with open(full_path, 'rb') as f:
                    print(data.hash_object(f.read()), full_path)
            if entry.is_dir(follow_symlinks=False):
                write_tree(full_path)

def is_ignored(path):
    return '.tgit' in path.split('/')

