# -*- coding: utf-8 -*-

# 格式：python main.py [原文文件] [抄袭版论文的文件] [答案文件]
# 均为绝对路径

# 返回参数
# -1：缺少参数
# -2：文件不存在
# -3：文件为空或无意义
# -4：文件编码错误
# -5：文件写入失败
# 0~1：相似度


import os
import sys

from vectoer_sim import similarity
from readandwrite import load, output
from generate_dict import generate_dict


def main(a):
    # 异常处理
    # 参数不足
    if len(a) < 4:
        print('缺少参数！')
        print('格式(均为绝对路径)：\npython main.py [原文文件] [抄袭版论文的文件] [答案文件]')
        return -1
    # 文件不存在
    if not os.path.exists(a[1]):
        print('原文文件不存在！\n')
        return -2
    if not os.path.exists(a[2]):
        print('抄袭版论文的文件不存在！')
        return -2

    orig = load(a[1])
    check = load(a[2])

    # 异常处理：空文件
    if orig == 0 or check == 0:
        print('文件为空或无意义！')
        return -3
    
    if orig == -1 or check == -1:
        print('请将文件另存为UTF-8或GBK编码！')
        return -4

    orig_dict = dict()
    check_dict = dict()

    orig_dict, check_dict = generate_dict(orig, check)

    # 将字典的值转换为列表，导入到相似度计算的函数中
    ans = similarity(list(orig_dict.values()), list(check_dict.values()))

    # print(ans)
    if(output(a[3], ans) == -1):
        print('相似度为：%.2f\n结果保存失败，请检查结果文件是否为只读！' % ans)
        return -5
    print('相似度为：%.2f，结果已保存至\"%s\"' % (ans, a[3]))
    return ans


if __name__ == '__main__':
    main(sys.argv)
