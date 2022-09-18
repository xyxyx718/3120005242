# -*- coding: utf-8 -*-

# 格式：python main.py [原文文件] [抄袭版论文的文件] [答案文件]
# 均为绝对路径

import sys
import jieba
import re
import numpy as np

a = sys.argv


def load(path):
    # 读取文件
    f = open(r'%s' % path, mode='r', encoding='utf-8')
    text = f.read()
    f.close()

    # 清理html格式、引号、中文中的空格
    text = re.sub(r'<.*?>', '', text, flags=re.S)
    text = re.sub(r'\s{2,}', '\n', text, flags=re.S)
    text = re.sub(r'''[“”‘’"'\(\)\{\}\[\]（）【】]''', '', text)
    text = re.sub(r'([\n] *)[a-zA-Z0-9.,;:!?_&\*\/\-\+\=↵<>]+( *[\n])', '', text)
    print(text)
    text = re.sub(r'(^[a-zA-Z0-9.,!?])[ \t]+(^[a-zA-Z0-9.,!?])', '', text)
    text = re.sub(r'(^[a-zA-Z0-9.,!?])[ \t]+(^[a-zA-Z0-9.,!?])', '', text)
    text = re.sub(r'(^[a-zA-Z0-9.,!?])[ \t]+(^[a-zA-Z0-9.,!?])', '', text)
    #print(text)
    return jieba.cut(text)


def output(path, ans):
    # 格式化并输出结果
    f = open(r'%s' % path, mode='w', encoding='utf-8')
    f.write('%.2f' % ans)
    f.close()


def similarity(a_array, b_array):
    # 计算两个向量夹角的余弦值
    # np.dot() 求两个一维数组的内积
    # linalg = linear（线性）+ algebra（代数），norm则表示范数
    # np.linagle.norm()即为求矩阵的二范数，即向量的模
    a_norm = np.linalg.norm(a_array)
    b_norm = np.linalg.norm(b_array)
    cos_oc = a_array.dot(b_array) / (a_norm * b_norm)
    # 考虑到cos是非线性的，并不直观，所以将其转换为线性的角度值
    arccos_oc = np.arccos(cos_oc)/np.pi*180
    # 计算向量距离
    dis = np.linalg.norm(a_array - b_array)
    # 处理后的角度和距离的加权平均
    sim = ((1-arccos_oc/90)+(1-dis/(a_norm+b_norm)))/2
    return sim


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

# 将字典的值转换为数组/多维向量
orig_array = np.array(list(orig_dict.values()))
check_array = np.array(list(check_dict.values()))

ans = similarity(orig_array, check_array)

print(ans)
# output(a[3], ans)
