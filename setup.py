from setuptools import setup, Extension, find_packages
# from Cython.Build import cythonize

ext_modules = [
    Extension(
        'cython_test.hello',
        sources=['cython_test/hello.pyx'],
    ),
    Extension(
        'cython_test.hello_printf',
        sources=['cython_test/hello_printf.pyx'],
    )
]

setup(
    name='cython_test',
    packages=find_packages(),
    # ext_modules=cythonize("cython_test/hello.pyx"),
    ext_modules=ext_modules,
    zip_safe=False,
)
