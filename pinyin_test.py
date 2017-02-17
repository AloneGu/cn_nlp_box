#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2/17/17 10:07 AM
# @Author  : Jackling 


from pypinyin import pinyin,lazy_pinyin,TONE,NORMAL

test_data = [u'你好',u'世界']

def trans_cn_pinyin(text):
    return ''.join(lazy_pinyin(text,NORMAL))


for r in test_data:
    print pinyin(r)
    print pinyin(r,NORMAL)
    print lazy_pinyin(r,TONE)
    print lazy_pinyin(r,NORMAL)
    print trans_cn_pinyin(r)
    print '----------'

