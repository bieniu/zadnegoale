#!/usr/bin/env python
from setuptools import setup


with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="zadnegoale",
    version="0.5.2",
    author="Maciej Bieniek",
    description="Python wrapper for getting allergen concentration data from Żadnego Ale servers.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    include_package_data=True,
    url="https://github.com/bieniu/zadnegoale",
    license="Apache-2.0 License",
    packages=["zadnegoale"],
    package_data={"nettigo_air_monitor": ["py.typed"]},
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
