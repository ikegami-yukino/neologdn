# -*- coding: utf-8 -*-
import re
from distutils.core import setup, Extension


with open('neologdn.cpp', 'r') as f:
    version = re.compile(
        r".*__version__ = '(.*?)'", re.S).match(f.read()).group(1)

setup(
    name='neologdn',
    version=version,
    description='Japanese text normalizer for mecab-neologd',
    long_description=open('README.rst').read()+open('CHANGES.rst').read(),
    author='Yukino Ikegami',
    author_email='yknikgm@gmail.com',
    url='http://github.com/ikegami-yukino/neologdn',
    ext_modules=[Extension('neologdn', ['neologdn.cpp'], language='c++')],
    license='Apache Software License',
    keywords=['japanese', 'MeCab'],
    classifiers=(
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Natural Language :: Japanese',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Cython',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Topic :: Text Processing :: Linguistic',
    )
)
