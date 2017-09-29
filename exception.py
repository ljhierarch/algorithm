#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
exception
~~~~~~~~~~~~

定制化的异常类集合

:copyright:  (c) 2017 zhihu
:authors: hanxinyu<hanxinyu@zhihu.com>
:version: 1.0 of 2017-09-22
'''


class QuitException(Exception):
    '''退出异常
    '''
    pass


class CommandNotFoundException(Exception):
    '''退出异常
    '''
    pass
