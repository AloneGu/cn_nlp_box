#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 1/25/17 10:12 AM
# @Author  : Jackling 

import pandas as pd
import jieba
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.tree import DecisionTreeClassifier


class TextCmdProcessor(object):
    def __init__(self, data_file):
        self.file_path = data_file
        self.src_df = pd.read_csv(self.file_path)
        print self.src_df.head()
        self.train_model()

    def train_model(self):
        self.vectorizer = CountVectorizer(min_df=0, analyzer=(lambda s: s.split()))
        str_x, x, y = [], [], []
        for text_row, cmd in self.src_df.values:
            split_str = ' '.join(jieba.cut(text_row, cut_all=True))
            str_x.append(split_str)
            y.append(int(cmd))
        x = self.vectorizer.fit_transform(str_x).toarray()
        self.model = DecisionTreeClassifier()
        self.model.fit(x, y)
        # for r in str_x:
        #     print r
        # for a,b in zip(x,y):
        #     print a,b

    def process(self, text):
        split_str = ' '.join(jieba.cut(text, cut_all=True))
        vec = self.vectorizer.transform([split_str]).toarray()
        return self.model.predict(vec)


if __name__ == '__main__':
    t = TextCmdProcessor('./data/train.csv')
    print t.process(u'关灯')
