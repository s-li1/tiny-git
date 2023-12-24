import hashlib
import os

TGIT_DIR = '.tgit'
NULL = b'\x00'

def init():
    os.mkdir(TGIT_DIR)
    os.mkdir(os.path.join(TGIT_DIR, 'objects'))

def hash_object(data, type='blob'):
    obj = type.encode() + NULL + data
    oid = hashlib.sha1(obj).hexdigest()
    with open(os.path.join(TGIT_DIR, 'objects', oid), 'wb') as f_obj:
        f_obj.write(obj)
    return oid

def get_object(oid, expected=None):
    with open(os.path.join(TGIT_DIR, 'objects', oid), 'rb') as f_obj:
            obj = f_obj.read()
    
    type, _, content = obj.partition(NULL)
    type = type.decode()

    if expected is not None and type != expected:
        raise ValueError(f'Expected {expected}, got {type}')

    return content
