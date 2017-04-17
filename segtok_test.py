#!/usr/bin/env python
# encoding: utf-8

"""
@author: Jackling Gu
@file: segtok_test.py
@time: 2017-04-17 16:49
"""

from segtok.segmenter import split_single, split_multi

test = ['s parent directory is not owned by the current user and caching wheels has been disabled.',
        ' check the permissions and owner of that directory. If executing pip with sudo, you may want sudo']

for t in test:
    print('_'.join(split_single(t)))
    print('_'.join(split_multi(t)))
