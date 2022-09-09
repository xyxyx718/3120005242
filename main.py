# -*- coding: utf-8 -*-

#格式：python main.py [原文文件] [抄袭版论文的文件] [答案文件]
#均为绝对路径

import sys

a = sys.argv

def load(a):
    f = open(r'%s' %a , mode='r',encoding='utf-8')
    l = f.read()
    f.close()
    return l

p = load(a[1])
print(p)