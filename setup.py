#!/usr/bin/env python3
 
from setuptools import setup
 
setup(name = 'tgit',
    version = '1.0',
    packages = ['tgit'],
    entry_points = {
        'console_scripts' : [
            'tgit = tgit.cli:main'
        ]
    }
)
