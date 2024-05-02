#!/bin/sh

if ! `type cython &> /dev/null`; then
    pip install cython
fi
cython --cplus -3 neologdn.pyx
