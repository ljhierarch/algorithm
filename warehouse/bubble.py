#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
warehouse.bubble
~~~~~~~~~~~~

冒泡排序

:copyright:  (c) 2017 zhihu
:authors: hanxinyu<hanxinyu@zhihu.com>
:version: 1.0 of 2017-09-29
'''

from warehouse.base import BaseAlgorithm


class BubbleAlgorithm(BaseAlgorithm):
    '''冒泡排序实现
    '''

    name = 'bubble'

    def achieve(self):
        '''执行
        '''
        length, trip_num, self.result = len(self.data), 1, self.data

        while trip_num < length:
            index, boundary = 0, length - trip_num
            while index < boundary:
                if self.result[index] < self.result[index + 1]:
                    tmp = self.result[index]
                    self.result[index] = self.result[index + 1]
                    self.result[index + 1] = tmp
                index = index + 1
            trip_num = trip_num + 1
