# -*- coding: utf-8 -*-

import numpy as np


def similarity(a_list: list, b_list: list):
    a_array = np.array(a_list)
    b_array = np.array(b_list)
    # linalg = linear（线性）+ algebra（代数），norm则表示范数
    # np.linagle.norm()即为求矩阵的二范数，即向量的模
    a_norm = np.linalg.norm(a_array)
    b_norm = np.linalg.norm(b_array)
    # 计算两个向量夹角的余弦值
    # np.dot() 求两个一维数组的内积
    cos_oc = a_array.dot(b_array) / (a_norm * b_norm)
    # 考虑到cos是非线性的，并不直观，所以将其转换为线性的角度值
    arccos_oc = np.arccos(cos_oc)/np.pi*180
    # 计算向量距离
    dis = np.linalg.norm(a_array - b_array)
    # 处理后的角度和距离的加权平均
    sim = (1-arccos_oc/90)*0.8 + (1-dis/(a_norm+b_norm))*0.2
    return sim
