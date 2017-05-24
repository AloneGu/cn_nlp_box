#!/usr/bin/env python
# encoding: utf-8

"""
@author: Jackling Gu
@file: intent_cls.py
@time: 2017-05-23 15:19
"""

import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import cross_val_score, StratifiedKFold, train_test_split
from sklearn.metrics import classification_report
import util


class TimerIntentClassification(object):
    def __init__(self):
        # init model
        self.rf_model = RandomForestClassifier()
        self.text_vec = CountVectorizer()
        self.le = LabelEncoder()

    def train(self, x, y):
        # x,y are text list
        trans_y = self.le.fit_transform(y)
        trans_x = self.text_vec.fit_transform(x).toarray()

        # cross check
        tmp_model = RandomForestClassifier()
        scores = cross_val_score(tmp_model, trans_x, trans_y,
                                 cv=StratifiedKFold(shuffle=True, n_splits=5, random_state=2333))
        print(list(scores), sum(scores))

        # train model
        train_x, _, train_y, _ = train_test_split(trans_x, trans_y, random_state=2333, test_size=0.2)
        self.rf_model.fit(train_x, train_y)
        print('train done')
        pred = self.rf_model.predict(trans_x)
        print(classification_report(trans_y, pred))

    def predict(self, x):
        # x is a text
        trans_x = self.text_vec.transform([x])
        res_y = self.rf_model.predict(trans_x)
        return self.le.inverse_transform(res_y)[0]

    def predict_many(self, x_list):
        trans_x = self.text_vec.transform(x_list)
        res_y = self.rf_model.predict(trans_x)
        return list(self.le.inverse_transform(res_y))


if __name__ == '__main__':
    x, y = [], []
    intent_x, intent_y = util.get_timer_data()
    x = intent_x
    y = intent_y
    misc_x, misc_y = util.get_misc_data()
    x = x + misc_x
    y = y + misc_y

    # jieba cut all
    intent_class = TimerIntentClassification()
    tmp_x = [' '.join(util.simple_split(t)) for t in x]
    intent_class.train(tmp_x, y)
    random_idx = np.random.choice(100, 10, replace=False)
    print([intent_class.predict(tmp_x[idx]) for idx in random_idx])
    print([y[idx] for idx in random_idx])
    print('======================= cut all')

    # jieba cut simple
    intent_class = TimerIntentClassification()
    tmp_x = [' '.join(util.simple_split(t, False)) for t in x]
    intent_class.train(tmp_x, y)
    print([intent_class.predict(tmp_x[idx]) for idx in random_idx])
    print([y[idx] for idx in random_idx])
    print('======================= cut simple')

    # 2 gram
    intent_class = TimerIntentClassification()
    tmp_x = [' '.join(util.gram_cut(t, 2)) for t in x]
    intent_class.train(tmp_x, y)
    print([intent_class.predict(tmp_x[idx]) for idx in random_idx])
    print([y[idx] for idx in random_idx])
    print('======================= 2 gram')

    # 2 gram and 1 gram
    intent_class = TimerIntentClassification()
    tmp_x = [' '.join(util.complex_gram_cut(t)) for t in x]
    intent_class.train(tmp_x, y)
    print([intent_class.predict(tmp_x[idx]) for idx in random_idx])
    print([y[idx] for idx in random_idx])
    print('======================= complex 2 gram')

    # 3 gram
    intent_class = TimerIntentClassification()
    tmp_x = [' '.join(util.gram_cut(t, 3)) for t in x]
    intent_class.train(tmp_x, y)
    print([intent_class.predict(tmp_x[idx]) for idx in random_idx])
    print([y[idx] for idx in random_idx])
    print('======================= 3 gram')

    # 3 gram and 1 gram
    intent_class = TimerIntentClassification()
    tmp_x = [' '.join(util.complex_gram_cut(t, 3)) for t in x]
    intent_class.train(tmp_x, y)
    print([intent_class.predict(tmp_x[idx]) for idx in random_idx])
    print([y[idx] for idx in random_idx])
    print('======================= 3 gram')
