#!/usr/bin/env python

from setuptools import setup
from alerce_base_model import __version__

with open("requirements.txt") as f:
    required_packages = f.readlines()

packages = [
    "alerce_base_model",
    "alerce_base_model.core"
]

setup(
    name="alerce_base_model",
    version=__version__,
    description="",
    author="ALeRCE Team",
    author_email='contact@alerce.online',
    packages=packages,
    install_requires=required_packages
)
