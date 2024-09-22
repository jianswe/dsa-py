# setup.py

from setuptools import setup, find_packages

setup(
    name='dsa-py',
    version='0.1',
    packages=find_packages(),
    install_requires=[],
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            # Add entry points here if needed
        ],
    },
)