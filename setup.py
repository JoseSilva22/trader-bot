from setuptools import setup
from pathlib import Path

with Path('README.md').open('r') as f:
    long_description = f.read()

with Path('requirements.txt').open('r') as f:
    requires = f.read().splitlines()

setup(
    name='proTrader',
    version='0.1',
    author='KinglordOfBaldness',
    author_email='zeeeee.miguel@gmail.com',
    description="Trader Bot Coinbase Pro",
    long_description=long_description,
    long_description_content_type="text/markdown",
    install_requires=requires,
    license='MIT',
    python_requires='>=3.7',
    classifiers=[
        "Programming Language :: Python :: 3",
        "Development Status :: 4 - Beta",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ]
)