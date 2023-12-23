import hashlib
import os

TGIT_DIR = '.tgit'

def init():
    os.mkdir(TGIT_DIR)
    os.mkdir(os.path.join(TGIT_DIR, 'objects'))

def hash_object(data):
    oid = hashlib.sha1(data).hexdigest()
    with open(os.path.join(TGIT_DIR, 'objects', oid), 'wb') as f_obj:
        f_obj.write(data)
    return oid

def get_object(oid):
    with open(os.path.join(TGIT_DIR, 'objects', oid), 'rb') as f_obj:
        return f_obj.read()
