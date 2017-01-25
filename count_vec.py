#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 1/25/17 10:12 AM
# @Author  : Jackling 


from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer

# test countvectorizer
vectorizer = CountVectorizer(min_df=1)
corpus = [
    'This is the first document.',
    'This is the second second document.',
    'And the third one.',
    'Is this the first document?',
]
analyze = vectorizer.build_analyzer()
print  analyze("This is a text document to analyze.")
X = vectorizer.fit_transform(corpus)
print vectorizer.get_feature_names()
print X.toarray()

# test cn
cn_corpus = [
    '有点 看不清',
    '把 灯 关闭'
]
vectorizer = CountVectorizer(min_df=0, analyzer=(lambda s: s.split()))
X = vectorizer.fit_transform(cn_corpus)
res = '/'.join(vectorizer.get_feature_names())
print res
print X.toarray()

# test td idf
vectorizer = TfidfVectorizer(min_df=1)
X = vectorizer.fit_transform(corpus)
print X.toarray()
