# -*- coding: utf-8 -*-

print("Hello world!")
print("from ipad")

import sys
print(sys.argv[0])

import jieba
import re

text = '设计一个论文查重算法。'
text_plus = jieba.cut(text)
for item in text_plus:
    print(item, end=' ')

text = '设计 一个 论文 查重 算法 。'
space_patten = re.compile(r'([^a-zA-Z0-9.,!?])[ \t]+([^a-zA-Z0-9.,!?])')
text = space_patten.sub(r'\1\2', text)
text = space_patten.sub(r'\1\2', text)
print(text)


from vectoer_sim import similarity
list1 = [1, 1, 4, 5, 1, 4, 0]
list2 = [1, 9, 1, 9, 8, 1, 0]
print(similarity(list1, list2))