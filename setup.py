#!/usr/bin/env python

from setuptools import setup, find_packages
from alerce_base_model import __version__

with open("requirements.txt") as f:
    required_packages = f.readlines()

required_packages = [r for r in required_packages if "-e" not in r]

setup(
    name="alerce_base_model",
    version=__version__,
    description="",
    author="ALeRCE Team",
    author_email='contact@alerce.online',
    packages=find_packages(),
    install_requires=required_packages
)
