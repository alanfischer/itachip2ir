"""A setuptools based setup module.
See:
https://packaging.python.org/en/latest/distributing.html
https://bitbucket.com/pallindo/itachip2ir
"""

from setuptools import setup, Extension
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

module = Extension('itachip2ir',
                    sources = [
                        'source/ITachIP2IR.cpp',
                        'source/IRCommandParser.cpp'
                    ])

setup(
    name='pyitachip2ir2',
    version='0.0.8',
    description='A library for sending IR commands to an ITach IP2IR gateway',
    long_description=long_description,
    url='https://github.com/alanfischer/itachip2ir',
    author='Alan Fischer',
    author_email='alan@spearfischer.net',
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Home Automation',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'Programming Language :: Python :: 3.13',
    ],
    keywords='itach ip2ir homeautomation',
    python_requires='>=3.9',
    py_modules = ["pyitachip2ir"],
    ext_modules = [module]
)
