# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

try:
    long_description = open("README.rst").read()
except IOError:
    long_description = ""

setup(
    name="CommentBot",
    version="0.1.0",
    description="Runs comment of the week on Reddit. ",
    license="MIT",
    author="iro",
    packages=find_packages(),
    install_requires=[],
    long_description=long_description,
    scripts=["scripts/commentoftheweek"],
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.6",
    ]
)
