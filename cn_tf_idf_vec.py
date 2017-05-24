#!/usr/bin/env python
# encoding: utf-8

"""
@author: Jackling Gu
@file: cn_tf_idf_vec.py
@time: 2017-04-18 10:25
"""

from sklearn.feature_extraction.text import CountVectorizer
import numpy as np

cn_corpus = [
    '有点 看不清',
    '把 灯 关闭',
    '测试 语料库',
    '中国 天气'
]
vectorizer = CountVectorizer(min_df=0, analyzer=(lambda s: s.split()))
X = vectorizer.fit_transform(cn_corpus)
res = '/'.join(vectorizer.get_feature_names())
print(res)
print(X.toarray())

test = '测试语料库'
import jieba.analyse

res = jieba.analyse.extract_tags(test,topK=None)
print(res)
res = jieba.analyse.extract_tags(test,topK=None,withWeight=True)
print(res)
res = jieba.analyse.extract_tags(test,topK=None,withFlag=True)
print(res)

feature_names = vectorizer.get_feature_names()
print(feature_names)
weight_vec = []
for w in feature_names:
    tmp_res = jieba.analyse.extract_tags(w, withWeight=True)
    print(tmp_res)
    if len(tmp_res)>0:
        weight_vec.append(tmp_res[0][1])
    else:
        weight_vec.append(1)
weight_vec = np.array(weight_vec)
print(weight_vec)

for x in X.toarray():
    print(x,np.round(x*weight_vec,2))

