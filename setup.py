#!/usr/bin/env python
# Copyright (c) 2017 pandas-gbq Authors All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.

# -*- coding: utf-8 -*-

import io
import os

import setuptools


# Package metadata.

name = "pandas-gbq"
description = "Google BigQuery connector for pandas"

# Should be one of:
# 'Development Status :: 3 - Alpha'
# 'Development Status :: 4 - Beta'
# 'Development Status :: 5 - Production/Stable'
release_status = "Development Status :: 4 - Beta"
dependencies = [
    "setuptools",
    "db-dtypes >=0.3.1,<2.0.0",
    "numpy >=1.16.6",
    "pandas >=0.24.2",
    "pyarrow >=3.0.0, <9.0dev",
    "pydata-google-auth",
    # Note: google-api-core and google-auth are also included via transitive
    # dependency on google-cloud-bigquery, but this library also uses them
    # directly.
    "google-api-core >= 1.31.5, <3.0.0dev,!=2.0.*,!=2.1.*,!=2.2.*,!=2.3.0",
    "google-auth >=1.25.0",
    "google-auth-oauthlib >=0.0.1",
    # Require 1.27.* because it has a fix for out-of-bounds timestamps.  See:
    # https://github.com/googleapis/python-bigquery/pull/209 and
    # https://github.com/googleapis/python-bigquery-pandas/issues/365
    # Exclude 2.4.* because it has a bug where waiting for the query can hang
    # indefinitely. https://github.com/pydata/pandas-gbq/issues/343
    "google-cloud-bigquery >=1.27.2,<4.0.0dev,!=2.4.*",
    "google-cloud-bigquery-storage >=1.1.0,<3.0.0dev",
]
extras = {
    "tqdm": "tqdm>=4.23.0",
}

# Setup boilerplate below this line.

package_root = os.path.abspath(os.path.dirname(__file__))

readme_filename = os.path.join(package_root, "README.rst")
with io.open(readme_filename, encoding="utf-8") as readme_file:
    readme = readme_file.read()

version = {}
with open(os.path.join(package_root, "pandas_gbq/version.py")) as fp:
    exec(fp.read(), version)
version = version["__version__"]

# Only include packages under the 'google' namespace. Do not include tests,
# benchmarks, etc.
packages = [
    package
    for package in setuptools.PEP420PackageFinder.find()
    if package.startswith("pandas_gbq")
]


setuptools.setup(
    name=name,
    version=version,
    description=description,
    long_description=readme,
    author="pandas-gbq authors",
    author_email="googleapis-packages@google.com",
    license="BSD-3-Clause",
    url="https://github.com/googleapis/python-bigquery-pandas",
    classifiers=[
        release_status,
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: BSD License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Operating System :: OS Independent",
        "Topic :: Internet",
        "Topic :: Scientific/Engineering",
    ],
    platforms="Posix; MacOS X; Windows",
    packages=packages,
    install_requires=dependencies,
    extras_require=extras,
    python_requires=">=3.7, <3.11",
    include_package_data=True,
    zip_safe=False,
)
