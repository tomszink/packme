from setuptools import setup

setup(
    name='packme',
    description='A minimal yet meaningful Python project setup',
    author='tomszink',
    package_dir={"": "src"},  # for all packages, look into ./src/*
    packages=['packme'],
)
