
#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
from setuptools import find_packages, setup

import vfs

setup(
    name='vfs',
    version=vfs.__version__,
    description='Video Frame Stacker',
    url='https://github.com/tna76874/vfs.git',
    author='maaaario',
    author_email='',
    license='BSD 2-clause',
    packages=find_packages(),
    install_requires=[
        "glob2",
        "argparse",
        "opencv-python",
    ],
    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: BSD License',  
        'Operating System :: POSIX :: Linux',        
        'Programming Language :: Python :: 3.7',
    ],
    python_requires = ">=3.7",
    entry_points={
        "console_scripts": [
            "vfs = vfs.vfs:main",
        ],
    },
    )