"""Pandoc filter for variable substitution using Mustache syntax

See:
https://github.com/michaelstepner/pandoc-mustache/
"""

from setuptools import setup, find_packages

# To use a consistent encoding
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
try:
    with open(path.join(here, "README.rst"), encoding="utf-8") as f:
        long_description = f.read()
except (IOError):
    with open(path.join(here, "README.md"), encoding="utf-8") as f:
        long_description = f.read()

version = {}
with open("pandoc_mustache/version.py") as fp:
    exec(fp.read(), version)
version = version["__version__"]

with open("requirements/prod.txt") as prod_requirements_file:
    PROD_REQUIREMENTS = prod_requirements_file.read().splitlines()

setup(
    name="pandoc-mustache",
    # Versions should comply with PEP440.  For a discussion on single-sourcing
    # the version across setup.py and the project code, see
    # https://packaging.python.org/en/latest/single_source_version.html
    version=version,
    description="Pandoc filter for variable substitution using Mustache syntax",
    long_description=long_description,
    # The project's main homepage.
    url="https://github.com/michaelstepner/pandoc-mustache/",
    # Original Author details
    # author="Michael Stepner",
    # author_email="stepner@mit.edu",
    # Choose your license
    license="CC0-1.0",
    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        "Development Status :: 4 - Beta",
        # Indicate who your project is intended for
        "Environment :: Console",
        "Intended Audience :: End Users/Desktop",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Build Tools",
        "Topic :: Text Processing :: Filters",
        "Operating System :: OS Independent",
        # Pick your license as you wish (should match "license" above)
        "License :: CC0 1.0 Universal (CC0 1.0) Public Domain Dedication",
        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        # https://pypi.python.org/pypi?%3Aaction=list_classifiers
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    # What does your project relate to?
    keywords="pandoc pandocfilters panflute markdown latex mustache",
    packages=find_packages(exclude=["contrib", "docs", "tests", "examples"]),
    install_requires=PROD_REQUIREMENTS,
    entry_points={
        "console_scripts": [
            "pandoc-mustache=pandoc_mustache.pandoc_mustache:main",
        ],
    },
    python_requires="~=3.7",
)
