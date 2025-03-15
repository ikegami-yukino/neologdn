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
      ext_modules=[
          Extension('neologdn', ['neologdn.cpp'],
                    language='c++',
                    extra_compile_args=extra_compile_args)
      ]
)
