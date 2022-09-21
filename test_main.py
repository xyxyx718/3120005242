# -*- coding: utf-8 -*-

import pytest

from main import *
from vectoer_sim import *
from readandwrite import *
from generate_dict import *


def test_load_empty():
    assert load(r'测试样例\空文件.txt') == 0

def test_load_coding_1():
    assert load(r'测试样例\正常_GBK.txt')

def test_load_coding_2():
    assert load(r'测试样例\正常.png') == -1

def test_output_writable():
    assert output(r'测试样例\ans_只读.txt', r'只读测试') == -1


def test_main_lack():
    assert main(['main.py', r'测试样例\正常.txt', r'ans.txt']) == -1

def test_main_nonexist_1():
    assert main(['main.py', r'测试样例\不存在.txt',
                r'测试样例\空文件.txt', r'ans.txt']) == -2

def test_nonexist_main_2():
    assert main(['main.py', r'测试样例\正常.txt', r'测试样例\不存在.txt', r'ans.txt']) == -2

def test_main_empty():
    assert main(['main.py', r'测试样例\正常.txt', r'测试样例\空文件.txt', r'ans.txt']) == -3

def test_main_coding():
    assert main(['main.py', r'测试样例\正常.txt', r'测试样例\正常.png', r'ans.txt']) == -4

def test_main_writable():
    assert main(['main.py', r'测试样例\正常.txt',
                r'测试样例\正常.txt', r'测试样例\ans_只读.txt']) == -5


def test_generate_dict():
    list1 = [1, 1, 4, 5, 1, 4]
    list2 = [1, 9, 1, 9, 8, 1, 0]
    assert generate_dict(list1, list2) == (
        {1: 3, 4: 2, 5: 1, 9: 0, 8: 0, 0: 0}, {1: 3, 4: 0, 5: 0, 9: 2, 8: 1, 0: 1})

def test_similarity():
    list1 = [1, 1, 4, 5, 1, 4, 0]
    list2 = [1, 9, 1, 9, 8, 1, 0]
    sim = similarity(list1, list2)
    assert abs(sim - 0.44) < 0.05


def test_main_copy():
    assert main(['main.py', '测试样例\正常.txt', '测试样例\正常.txt', 'ans.txt']) > 0.99

def test_main_sim():
    assert abs(
        main(['main.py', '测试样例\正常.txt', '测试样例\抄袭.txt', 'ans.txt']) - 0.81) < 0.05

def test_main_diff():
    assert main(['main.py', '测试样例\正常.txt', '测试样例\没抄袭.txt', 'ans.txt']) < 0.4
