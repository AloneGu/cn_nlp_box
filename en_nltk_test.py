#!/usr/bin/env python
# encoding: utf-8

"""
@author: Jackling Gu
@file: en_nltk_test.py
@time: 2017-04-17 12:30
"""


test_txt = "Previous chapters have shown you how to process and analyse text corpora, " \
           "and we have stressed the challenges for NLP in dealing with the vast amount of " \
           "electronic language data that is growing daily. Let's consider this data more closely, " \
           "and make the thought experiment that we have a gigantic corpus consisting of everything " \
           "that has been either uttered or written in English over, say, the last 50 years. " \
           "Would we be justified in calling this corpus 'the language of modern English'? " \
           "There are a number of reasons why we might answer No. Recall that in 3, we asked you " \
           "to search the web for instances of the pattern the of. Although it is easy to find examples " \
           "on the web containing this word sequence."
import nltk

token_list = nltk.word_tokenize(test_txt)

print(token_list)
print('-----')

from nltk.stem.porter import PorterStemmer
porter_stemmer = PorterStemmer()
print(porter_stemmer.stem('maximum'))
print(porter_stemmer.stem('presumably'))
print(porter_stemmer.stem('maximum presumably'))
print(porter_stemmer.stem('used ate maximum presumably'))
print('-----')


from nltk.stem import WordNetLemmatizer
wordnet_lemmatizer = WordNetLemmatizer()
print(wordnet_lemmatizer.lemmatize('dogs'))
print(wordnet_lemmatizer.lemmatize('churches'))
print(wordnet_lemmatizer.lemmatize('churches presumably'))
print(wordnet_lemmatizer.lemmatize('presumably'))
print(wordnet_lemmatizer.lemmatize('ate'))
print(wordnet_lemmatizer.lemmatize('used',pos='v'))
print('-----')

from nltk.corpus import stopwords
en_st_words = stopwords.words('english')
print(stopwords.words('english')[:10])
print('-----')

new_t = [w.lower() for w in token_list if w.lower() not in en_st_words and w.isalpha()]
print(new_t)
print('-----')
