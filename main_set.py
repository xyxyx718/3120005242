# -*- coding: utf-8 -*-

# 格式：python main.py [原文文件] [抄袭版论文的文件] [答案文件]
# 均为绝对路径

import sys
import jieba
import re

a = sys.argv


def load(a):
    f = open(r'%s' % a, mode='r', encoding='utf-8')
    text = f.read()
    f.close()

    text = re.sub(r'\s', '', text)
    text = re.sub(r'<.*?>', '', text)
    text = re.sub(r'''[“”‘’"']''', '', text)
    #text = re.sub(r'[a-zA-Z0-9]*', '', text)
    return jieba.cut(text)


def jaccard_similarity(A, B):
    # 求集合 A 和集合 B 的交集
    nominator = A.intersection(B)
    # 求集合 A 和集合 B 的并集
    denominator = A.union(B)
    # 计算比率
    similarity = len(nominator)/len(denominator)
    return similarity


orig = load(a[1])
check = load(a[2])
orig_set = set(orig)
check_set = set(check)
similarity = jaccard_similarity(orig_set, check_set)


print(similarity)
