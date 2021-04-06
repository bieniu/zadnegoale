#!/usr/bin/env python
from setuptools import setup

setup(
    name="zadnegoale",
    version="0.2.1",
    author="Maciej Bieniek",
    author_email="maciej.bieniek@gmail.com",
    description="Python wrapper for getting allergen concentration data from Żadnego Ale servers.",
    include_package_data=True,
    url="https://github.com/bieniu/zadnegoale",
    license="Apache-2.0 License",
    packages=["zadnegoale"],
    python_requires=">=3.6",
    install_requires=list(val.strip() for val in open("requirements.txt")),
    classifiers=[
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python",
        "Operating System :: OS Independent",
    ],
    setup_requires=("pytest-runner"),
    tests_require=list(val.strip() for val in open("requirements-test.txt")),
)
