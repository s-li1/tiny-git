import os
from . import data

def write_tree(directory='.'):
    entries = []
    with os.scandir(directory) as it:
        for entry in it:
            full_path = os.path.join(directory, entry.name)
            if is_ignored(full_path):
                continue
            if entry.is_file(follow_symlinks=False):
                type_ = 'blob' 
                with open(full_path, 'rb') as f:
                    oid = data.hash_object(f.read())
            elif entry.is_dir(follow_symlinks=False):
                type_ = 'tree'
                oid = write_tree(full_path)
            entries.append((entry.name, oid, type_))

    tree = ''.join(f'{type_} {oid} {name}\n' for name, oid, type_ in sorted(entries))

    return data.hash_object(tree.encode(), 'tree')

def is_ignored(path):
    return '.tgit' in path.split('/')

