__author__ = "Thomas D. Fischer"

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(name="gpsbro",
      author="Thomas D. Fischer",
      version="0.0.1",
      py_modules=["gpsbro",
                  "gpsbro.geonet",
                  "gpsbro.geonet.rinex",
                  "gpsbro.geonet.marks",
                  "gpsbro.geonet.test",],
      )
