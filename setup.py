# -*- coding: UTF-8 -*
# SEE: https://setuptools.pypa.io/en/latest/userguide/pyproject_config.html
# SEE: https://pypi.org/classifiers/
"""
Setup script for "behave4cmd0".

USAGE:
    python setup.py sdist
    python setup.py install
"""

from __future__ import absolute_import, print_function
import os.path
from setuptools import find_packages, setup


# -----------------------------------------------------------------------------
# UTILITY:
# -----------------------------------------------------------------------------
def find_packages_by_root_package(where):
    """
    Better than excluding everything that is not needed,
    collect only what is needed.
    """
    root_package = os.path.basename(where)
    packages = [ "%s.%s" % (root_package, sub_package)
                 for sub_package in find_packages(where)]
    packages.insert(0, root_package)
    return packages


# ----------------------------------------------------------------------------
# PROJECT CONFIGURATION (for sdist/setup mostly):
# ----------------------------------------------------------------------------
HERE = os.path.dirname(__file__) or os.curdir
THIS_PACKAGE_DIR = os.path.join(HERE, "behave4cmd0")


# ----------------------------------------------------------------------------
# TASK CONFIGURATION:
# ----------------------------------------------------------------------------
setup(
    name="behave4cmd0",
    version= "1.2.7.dev5",
    url="https://github.com/behave/behave4cmd0",
    author="Jens Engel",
    author_email="jenisys@noreply.github.com",
    license="BSD",
    description = "Provides a step-library for `behave <https://pypi.org/project/behave>`_ for testing commands/CLI apps.",
    # PREPARED: long_description = ""
    keywords = ["behave", "behave step-library", "console", "CLI", "testing", "BDD"],
    platforms  = [ 'any' ],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Framework :: Behave",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Topic :: Software Development :: Testing",
        "Topic :: Software Development :: Testing :: BDD",
        "Topic :: Terminals",
    ],
    provides=["behave4cmd0"],
    packages=find_packages_by_root_package(THIS_PACKAGE_DIR),

    # -- REQUIREMENTS:
    # SUPPORT: python2.7 (python2 only)
    python_requires=">=2.7, !=3.0.*, !=3.1.*, !=3.2.*",
    install_requires=[
        # -- PREPARED-FOR-FUTURE: "behave >= 1.2.6",
        "enum34; python_version < '3.4'",
        "six >= 1.15.0",
        # -- ASSERTION MATCHERS:
        "assertpy >= 1.1",
        "PyHamcrest >= 2.0.2; python_version >= '3.0'",
        "PyHamcrest <  2.0;   python_version <  '3.0'",
    ],
    tests_require=[
        "pytest <  5.0; python_version <  '3.0'",
        "pytest >= 5.0; python_version >= '3.0'",
        "pytest-html >= 1.19.0,<2.0; python_version <  '3.0'",
        "pytest-html >= 2.0;         python_version >= '3.0'",
    ],
    # extra_requires= read_requirements("requirements-develop.txt"),
    include_package_data= True,
    zip_safe = True,
)
