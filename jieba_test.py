#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 1/25/17 10:12 AM
# @Author  : Jackling 


import jieba

seg_list = jieba.cut("我来到北京清华大学", cut_all=True)

print("Full Mode:", "/ ".join(seg_list))  # 全模式

seg_list = jieba.cut("我来到北京清华大学", cut_all=False)

print("Default Mode:", "/ ".join(seg_list))  # 精确模式

seg_list = jieba.cut("他来到了网易杭研大厦")  # 默认是精确模式
print(", ".join(seg_list))

seg_list = jieba.cut_for_search("小明硕士毕业于中国科学院计算所，后在日本京都大学深造")  # 搜索引擎模式
print(", ".join(seg_list))

seg_list = jieba.cut("我来到北京清华大学pm二点五是多少", cut_all=True)

print("Full Mode:", "/ ".join(seg_list))  # 全模式

seg_list = jieba.cut("我来到北京清华大学pm2.5是多少", cut_all=True)

print("Full Mode:", "/ ".join(seg_list))  # 全模式
