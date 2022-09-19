# -*- coding: utf-8 -*-

# 格式：python main.py [原文文件] [抄袭版论文的文件] [答案文件]
# 均为绝对路径

import os
import sys

from vectoer_sim import similarity
from readandwrite import load, output

a = sys.argv
# 异常处理
# 参数不足
if len(a)<4:
    print('缺少参数！')
    print('格式(均为绝对路径)：\npython main.py [原文文件] [抄袭版论文的文件] [答案文件]')
    exit(0)
# 文件不存在
if not os.path.exists(a[1]):
    print('原文文件不存在！')
    exit(0)
if not os.path.exists(a[2]):
    print('抄袭版论文的文件不存在！')
    exit(0)

orig = load(a[1])
check = load(a[2])

# 异常处理：空文件
if orig == 0 or check == 0:
    print('文件内容为空或无意义！')
    exit(0)

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

# 将字典的值转换为列表
ans = similarity(list(orig_dict.values()), list(check_dict.values()))

#print(ans)
output(a[3], ans)
