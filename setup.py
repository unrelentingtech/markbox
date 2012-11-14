#!/usr/bin/env python
import sys
from distutils.core import setup
from markbox import __version__

if sys.version < "2.5":
    sys.exit("Python 2.5 or higher is required")

setup(name="markbox",
      version="0.1.0",
      description="A blogging engine for Dropbox based on Markdown",
#      long_description="""""",
      license="Apache License 2.0",
      author="myfreeweb",
      author_email="floatboth@me.com",
      url="https://github.com/myfreeweb/markbox",
      requires=["pylibmc", "mockcache", "Jinja2", "dropbox", "markdown",
          "pygments", "bottle", "parsedatetime", "mdx_smartypants", "pyatom"],
      packages=["markbox"],
      keywords=["web", "http", "dropbox", "markdown", "blog"],
      classifiers=[
        "Environment :: Web Environment",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Topic :: Internet :: WWW/HTTP",
      ],
      package_data={},
)
