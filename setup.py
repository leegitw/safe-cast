#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#  @namespace safe_cast
#
#    Copyright (c) 2018 TUNE, Inc.
#    All rights reserved.
#

from __future__ import with_statement

# To install the tune-mv-integration-python library, open a Terminal shell,
# then run this file by typing:
#
# python setup.py install
#

import sys
import re
import codecs

from setuptools import setup

REQUIREMENTS = [
    req for req in open('requirements.txt')
    .read().split('\n')
    if req != ''
]

PACKAGES = [
    'safe_cast',
]

TEST_REQUIREMENTS = ['pytest>=3.5.0', 'pytest-cov']

with open('safe_cast/__init__.py', 'r') as fd:
    version = re.search(r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]', fd.read(), re.MULTILINE).group(1)

if not version:
    raise RuntimeError('Cannot find version information')

if len(sys.argv) < 2 or sys.argv[1] == 'version':
    print(version)
    sys.exit()

CLASSIFIERS = [
    # How mature is this project? Common values are
    #   3 - Alpha
    #   4 - Beta
    #   5 - Production/Stable
    'Development Status :: 5 - Production/Stable',
    'Intended Audience :: Developers',
    'Operating System :: OS Independent',
    'Natural Language :: English',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python',
    'Programming Language :: Python :: 2.7',
    'Programming Language :: Python :: 3.0',
    'Programming Language :: Python :: 3.1',
    'Programming Language :: Python :: 3.2',
    'Programming Language :: Python :: 3.3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: Implementation :: PyPy'
]

with codecs.open('README.rst', 'r', 'utf-8') as f:
    readme = f.read()
with codecs.open('HISTORY.rst', 'r', 'utf-8') as f:
    history = f.read()

setup(
    name='safe-cast',
    version=version,
    description='Safe casting of Python base types',
    long_description=readme + '\n\n' + history,
    author='TUNE Inc.',
    author_email='jefft@tune.com',
    url='https://github.com/TuneLab/safe-cast',
    download_url='https://github.com/TuneLab/safe-cast/archive/v{0}.tar.gz'.format(version),
    keywords="safe casting tune",
    license='MIT License',
    zip_safe=False,
    include_package_data=True,
    install_requires=REQUIREMENTS,
    packages=PACKAGES,
    package_data={'': ['LICENSE']},
    package_dir={'safe-cast': 'safe-cast'},
    setup_requires=[
        'pytest-runner',
    ],
    tests_require=TEST_REQUIREMENTS,
    classifiers=CLASSIFIERS
)
