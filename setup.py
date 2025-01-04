#!/usr/bin/env python
import os
import subprocess
from setuptools import setup, find_packages


CLASSIFIERS = [
    "Programming Language :: Python"
]

extra = {}
try:
    version_git = (
        os.getenv("GITPKGVTAG", None) or subprocess.check_output(["git", "rev-parse", "--short", "HEAD"]).rstrip()
    )
except (subprocess.CalledProcessError, OSError):
    version_git = "unknown"

extra["install_requires"] = open("requirements.txt").read().splitlines()

setup(
    name="tmdev",
    version=0.0,
    description="ToastMaster Digital Evaluation Forms",
    author="Gil Coelho",
    license="Vale do Sousa Toastmasters Club",
    keywords="Django Python Evaluation Forms",
    platforms="any",
    classifiers=CLASSIFIERS,
    packages=find_packages(exclude=["tests", "tests.*"]),
    use_scm_version=False,
    tests_require=["coverage"],
    **extra
)
