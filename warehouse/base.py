#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
warehouse.base
~~~~~~~~~~~~

算法实现基础类

:copyright:  (c) 2017 zhihu
:authors: hanxinyu<hanxinyu@zhihu.com>
:version: 1.0 of 2017-09-29
'''

import json
from warehouse import keeper


class AlgorithmMeta(type):
    '''算法类构建函数
    '''

    def __new__(meta, name, bases, dct):
        '''产生类实例
        '''
        return super(AlgorithmMeta, meta).__new__(meta, name, bases, dct)

    def __init__(cls, name, bases, dct):
        '''构建类实例
        '''
        super(AlgorithmMeta, cls).__init__(name, bases, dct)
        keeper.add_algorithm(cls)


class BaseAlgorithm(object):
    '''算法实现基础类
    '''

    __metaclass__ = AlgorithmMeta
    name = 'base'

    def __init__(self):
        '''初始化，构建执行时所需数据
        '''
        with open('./input.txt') as data_file:
            self.data = json.loads(data_file.read())
        self.result = None

    def execute(self):
        '''执行算法
        '''
        print '输入：', self.data
        self.achieve()
        print '输出: ', self.result

    def achieve(self):
        '''算法实现
        '''
        raise NotImplementedError

    @classmethod
    def self_introduct(cls):
        '''自我介绍
        '''
        with open('./docs/{}.txt'.format(cls.name)) as des_doc:
            print des_doc.read()
