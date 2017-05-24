## timer intent classification

* add
* edit
* cancel
* none

## output of intent_cls.py

```
Building prefix dict from /usr/local/lib/python3.5/dist-packages/jieba/dict.txt ...
Loading model from cache /tmp/jieba.cache
Loading model cost 1.9661221504211426 seconds.
Prefix dict has been built succesfully.
[0.83999999999999997, 0.83333333333333337, 1.0, 0.95652173913043481, 0.95238095238095233] 4.58223602484
train done
             precision    recall  f1-score   support

          0       1.00      0.89      0.94        19
          1       1.00      1.00      1.00        14
          2       0.94      1.00      0.97        16
          3       0.99      1.00      0.99        68

avg / total       0.98      0.98      0.98       117

['add', 'edit', 'none', 'add', 'add', 'add', 'add', 'add', 'add', 'add']
['add', 'add', 'add', 'add', 'add', 'add', 'add', 'add', 'add', 'add']
=======================
[0.92000000000000004, 0.875, 1.0, 1.0, 0.90476190476190477] 4.69976190476
train done
             precision    recall  f1-score   support

          0       1.00      0.95      0.97        19
          1       1.00      1.00      1.00        14
          2       1.00      1.00      1.00        16
          3       0.99      1.00      0.99        68

avg / total       0.99      0.99      0.99       117

['add', 'add', 'none', 'add', 'add', 'add', 'add', 'add', 'add', 'add']
['add', 'add', 'add', 'add', 'add', 'add', 'add', 'add', 'add', 'add']
=======================
[0.92000000000000004, 0.83333333333333337, 1.0, 1.0, 0.90476190476190477] 4.6580952381
train done
             precision    recall  f1-score   support

          0       1.00      0.95      0.97        19
          1       1.00      1.00      1.00        14
          2       1.00      1.00      1.00        16
          3       0.99      1.00      0.99        68

avg / total       0.99      0.99      0.99       117

['add', 'add', 'none', 'add', 'add', 'add', 'add', 'add', 'add', 'add']
['add', 'add', 'add', 'add', 'add', 'add', 'add', 'add', 'add', 'add']
=======================
[0.80000000000000004, 0.875, 1.0, 0.95652173913043481, 0.90476190476190477] 4.53628364389
train done
             precision    recall  f1-score   support

          0       1.00      0.95      0.97        19
          1       1.00      1.00      1.00        14
          2       1.00      1.00      1.00        16
          3       0.99      1.00      0.99        68

avg / total       0.99      0.99      0.99       117

['add', 'none', 'add', 'add', 'add', 'add', 'add', 'add', 'add', 'add']
['add', 'add', 'add', 'add', 'add', 'add', 'add', 'add', 'add', 'add']

```