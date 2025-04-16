### File: setup.py
from setuptools import setup, find_packages

setup(
    name='modmanager',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'toga>=0.4.0'
    ],
    entry_points={
        'console_scripts': [
            'modmanager = modmanager.app:main',
        ],
    },
)

