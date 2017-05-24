#!/usr/bin/env python
# encoding: utf-8

"""
@author: Jackling Gu
@file: util.py
@time: 2017-05-23 15:19
"""

import jieba
import pandas as pd


def simple_split(text, all_flag=True):
    cut_res = jieba.cut(text, cut_all=all_flag)
    return list(cut_res)


def gram_cut(text, gram=2):
    text_len = len(text)
    if text_len <= gram:
        return [text]
    if gram >= 2:
        return [text[i:i + gram] for i in range(text_len + 1 - gram)]
    else:  # gram = 1, tricks to expand char for vectorization
        return [t + 'END' for t in text]


def complex_gram_cut(text, gram=2):
    if gram < 2:
        raise Exception('gram must le 2')
    return gram_cut(text, 1) + gram_cut(text, gram)


def get_misc_data():
    """

    :return: none intent text and corresponding tag 'none'
    """
    data_f = 'data/misc.txt'
    none_txt_list = []
    with open(data_f) as fin:
        for row in fin.readlines():
            row = row.strip()
            new_row_list = row.split(',')
            for t in new_row_list:
                if len(t) > 2:
                    none_txt_list.append(t)
    return none_txt_list, ['none'] * len(none_txt_list)


def get_timer_data():
    data_f = 'data/timer.csv'
    df = pd.read_csv(data_f)
    return list(df.text.values), list(df.intent.values)


if __name__ == '__main__':
    # some test
    print(simple_split('你好世界'))
    print(gram_cut('你好世界'))
    print(gram_cut('你好世界', 2))
    print(gram_cut('你好世界', 3))
    print(gram_cut('你好世界', 10))
    print(complex_gram_cut('你好世界'))
    # print(complex_gram_cut('你好世界',1))
    y, y_tag = get_misc_data()
    print(y[:2], len(y))
    print(y_tag[:2])
    y, y_tag = get_timer_data()
    print(y[:2], len(y))
    print(y_tag[:2])
