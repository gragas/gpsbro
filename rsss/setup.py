__author__ = "Thomas D. Fischer"

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(name="rsss",
      author="Thomas D. Fischer",
      version="0.0.1",
      py_modules=["rsss",
                  "rsss.geonet",
                  "rsss.geonet.rinex",
                  "rsss.geonet.marks",
                  "rsss.geonet.test",],
      )
