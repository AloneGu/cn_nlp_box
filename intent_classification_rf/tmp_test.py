#!/usr/bin/env python
# encoding: utf-8

"""
@author: Jackling Gu
@file: tmp_test.py
@time: 2017-05-23 18:34
"""

texts_1 = ['你 好end', '世 界end']
texts = ['你 好', '世 界']  # will cause fail
from sklearn.feature_extraction.text import CountVectorizer

vec = CountVectorizer(analyzer='char')
print(vec.fit_transform(texts).toarray())
print(vec.get_feature_names())

vec = CountVectorizer(analyzer='word', tokenizer=lambda x: x.split(' '))
print(vec.fit_transform(texts).toarray())
print(vec.get_feature_names())

vec = CountVectorizer(analyzer='word', tokenizer=lambda x: x.split(' '))
print(vec.fit_transform(texts_1).toarray())
print(vec.get_feature_names())

vec = CountVectorizer(analyzer='word')
print(vec.fit_transform(texts_1).toarray())
print(vec.get_feature_names())

cn_corpus = [
    '有点 看不清',
    '把 灯 关闭'
]
vectorizer = CountVectorizer(analyzer=lambda s: s.split(' '))
X = vectorizer.fit_transform(cn_corpus)
res = '/'.join(vectorizer.get_feature_names())
print(X.toarray())
print(res)


from util import simple_split
texts_2 = ['开发者定义完数据处理模型后','D3会自动运行','动态处理数据']
process_texts_2 = [' '.join(simple_split(t)) for t in texts_2]
print(process_texts_2)
vec = CountVectorizer(analyzer='word')
print(vec.fit_transform(process_texts_2).toarray())
print(vec.get_feature_names())

print(process_texts_2)
vec = CountVectorizer(analyzer='word', tokenizer=lambda x:x.split(' '))
print(vec.fit_transform(process_texts_2).toarray())
print(vec.get_feature_names())

from keras.preprocessing.text import Tokenizer
tok = Tokenizer()
tok.fit_on_texts(process_texts_2)
print(tok.texts_to_matrix(process_texts_2,mode='count'))
print(tok.word_counts)
print(tok.word_docs)