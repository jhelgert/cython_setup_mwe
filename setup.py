#!/usr/bin/env python3

from setuptools import setup, Extension
from Cython.Build import cythonize

ext_modules = [
    Extension("my_package.a", ["my_package/a.pyx"]),
    Extension("my_package.b", ["my_package/b.pyx"])
]

setup(ext_modules=cythonize(ext_modules),
      packages=["my_package"],
      name="my_package",
      zip_safe=False)
