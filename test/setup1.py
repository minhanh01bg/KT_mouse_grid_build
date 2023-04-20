from setuptools import setup
import sys
from setuptools import setup, find_packages
import py2exe
with open('../requirements.txt') as f:
    requirements = f.read().splitlines()
setup(
    name="MyApp",
    version="1.0",
    author="Your Name",
    author_email="your.email@example.com",
    description="My tkinter app",
    options={"py2exe": {"bundle_files": 1, "packages": ["pynput"]}},
    windows=[{"script": "../main.py"}],
    zipfile=None,
    install_requires=requirements,
)
