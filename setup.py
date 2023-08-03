# -*- coding: utf-8 -*-
from codecs import open
import re
from setuptools import setup, Extension
import platform

with open('neologdn.cpp', 'r', encoding='utf8') as f:
    version = re.compile(r".*__version__ = '(.*?)'",
                         re.S).match(f.read()).group(1)

extra_compile_args = ["-std=c++11"]
if platform.system() == "Darwin":
    extra_compile_args.append("-mmacosx-version-min=10.7")
    extra_compile_args.append("-stdlib=libc++")

setup(name='neologdn',
      version=version,
      author='Yukino Ikegami',
      author_email='yknikgm@gmail.com',
      url='http://github.com/ikegami-yukino/neologdn',
      ext_modules=[
          Extension('neologdn', ['neologdn.cpp'],
                    language='c++',
                    extra_compile_args=extra_compile_args)
      ],
      license='Apache Software License',
      keywords=['japanese', 'MeCab'],
      classifiers=[
          'Development Status :: 3 - Alpha', 'Intended Audience :: Developers',
          'Natural Language :: Japanese',
          'License :: OSI Approved :: Apache Software License',
          'Programming Language :: Cython', 'Programming Language :: Python',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.6',
          'Programming Language :: Python :: 3.7',
          'Programming Language :: Python :: 3.8',
          'Programming Language :: Python :: 3.9',
          'Programming Language :: Python :: 3.10',
          'Programming Language :: Python :: 3.11',
          'Topic :: Text Processing :: Linguistic'
      ],
      description='Japanese text normalizer for mecab-neologd',
      long_description='%s\n\n%s' %
      (open('README.rst', 'r', encoding='utf8').read(),
       open('CHANGES.rst', 'r', encoding='utf8').read()),
      long_description_content_type='text/x-rst')
