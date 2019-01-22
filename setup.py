# coding: utf-8
import os
from setuptools import setup

PACKAGE_NAME = 'kenobi'
AUTHOR = 'Yoandy Rodriguez Martinez'
AUTHOR_EMAIL = "yoandy.rmartinez@gmail.com"
VERSION = "0.1"
LICENSE = "MIT"

package_root_dir = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(package_root_dir, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name=PACKAGE_NAME,
    version=VERSION,
    description='Python Language Server implementation',
    long_description=long_description,
    url="http://github.com/yorodm/kenobi",
    author=AUTHOR,
    keywords='lsp, complation',
    author_email=AUTHOR_EMAIL,
    license=LICENSE,
    packages=['kenobi'],
    install_requires=[
        'jedi',
        'pygls',
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Intended Audience :: Information Technology',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    zip_safe=False,
    entry_points={
        'console_scripts': ['kenobi=kenobi.cli:main']
    },
)
