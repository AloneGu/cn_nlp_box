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
    'and and and the'
    'Is this the first document?',
]
analyze = vectorizer.build_analyzer()
print(analyze("This is a text document to analyze."))
X = vectorizer.fit_transform(corpus)
print(vectorizer.get_feature_names())
print(X.toarray())
print('-' * 20)
# test countvectorizer
vectorizer = CountVectorizer(min_df=1, binary=True)
corpus = [
    'This is the first document.',
    'This is the second second document.',
    'And the third one.',
    'and and and the'
    'Is this the first document?',
]
analyze = vectorizer.build_analyzer()
print(analyze("This is a text document to analyze."))
X = vectorizer.fit_transform(corpus)
print(vectorizer.get_feature_names())
print(X.toarray())
print('-' * 20)
# test cn
cn_corpus = [
    '有点 看不清',
    '把 灯 关闭',
    '把 灯 打开'
]
vectorizer = CountVectorizer(min_df=0, analyzer=(lambda s: s.split()))
X = vectorizer.fit_transform(cn_corpus)
res = '/'.join(vectorizer.get_feature_names())
print(res)
print(X.toarray())
analyser = vectorizer.build_analyzer()
preprocessor = vectorizer.build_preprocessor()
tokenizer = vectorizer.build_tokenizer()
print(preprocessor('把灯打开'))
print(tokenizer('把灯打开'))
print(preprocessor('把 灯 打开'))
print(tokenizer('把 灯 打开'))


# test td idf
vectorizer = TfidfVectorizer(min_df=1)
X = vectorizer.fit_transform(corpus)
print(X.toarray())
print('-' * 20)

