#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
warehouse.keeper
~~~~~~~~~~~~

算法实现对外交互模块

:copyright:  (c) 2017 zhihu
:authors: hanxinyu<hanxinyu@zhihu.com>
:version: 1.0 of 2017-09-22
'''

# 算法仓库
algorithms = {}


def get_algorithm(name):
    '''根据名称获取算法
    '''

    return algorithms.get(name)


def add_algorithm(algorithm):
    '''将算法添加到算法仓库
    '''

    algorithms[algorithm.name] = algorithm
