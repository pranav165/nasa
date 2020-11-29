#!/usr/bin/env python3

VERSION = '1.0.0'
DESCRIPTION = 'NASA Coding Assignment'

try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup, find_packages

setup(
    name='nasa',
    version=VERSION,
    description=DESCRIPTION,
    license="NASA",
    long_description="Coding Assignment solution for NASA Problem",
    url='NA',
    author="Pranav Sharma",
    author_email='pranav165@gmail.com',
    install_requires=[
        'requests==2.24.0',
        'pytest==6.1.1',
        'pyhamcrest==2.0.2',
        'retry==0.9.2',
        'pytest-html==2.1.1',
        'wheel==0.35.1',
        'flake8==3.8.4'
    ],
    provides=[],
    packages=find_packages(),
    scripts=[]
)
