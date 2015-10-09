#!/bin/sh

if ! `type cython &> /dev/null`; then
    pip install cython
fi
cython --cplus neologdn.pyx
