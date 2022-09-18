# -*- coding: utf-8 -*-

# 格式：python main.py [原文文件] [抄袭版论文的文件] [答案文件]
# 均为绝对路径

import sys
import jieba
import re
import numpy as np

a = sys.argv


def load(path):
    f = open(r'%s' % path, mode='r', encoding='utf-8')
    text = f.read()
    f.close()

    text = re.sub(r'\s', '', text)
    text = re.sub(r'<.*?>', '', text)
    text = re.sub(r'''[“”‘’"']''', '', text)
    #text = re.sub(r'[a-zA-Z0-9]*', '', text)
    return jieba.cut(text)


def output(path, ans):
    f = open(r'%s' % path, mode='w', encoding='utf-8')
    f.write('%.2f' % ans)
    f.close()


orig = load(a[1])
check = load(a[2])
orig_dict = dict()
check_dict = dict()

# 生成字典
for item in orig:
    if item in orig_dict:
        orig_dict[item] += 1
    else:
        orig_dict[item] = 1
        check_dict[item] = 0

for item in check:
    if item in check_dict:
        check_dict[item] += 1
    else:
        check_dict[item] = 1
        orig_dict[item] = 0

# 将字典的值转换为数组
orig_array = np.array(list(orig_dict.values()))
check_array = np.array(list(check_dict.values()))

# 计算两个多维向量的余弦值
# np.dot() 求两个一维数组的内积
# linalg = linear（线性）+ algebra（代数），norm则表示范数
# np.linagle.norm()即为求矩阵的二范数，即平方和开根号
cos_oc = orig_array.dot(check_array) / \
    (np.linalg.norm(orig_array)*np.linalg.norm(check_array))

output(a[3], cos_oc)
