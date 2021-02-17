import numpy
from setuptools import setup
from Cython.Build import cythonize

setup(
    name='Noise_reductor',
    ext_modules=cythonize("cython_cygno.pyx"),
    include_dirs=[numpy.get_include()],
    zip_safe=False,
)
