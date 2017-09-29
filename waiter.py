#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
waiter
~~~~~~~~~~~~

项目执行入口

:copyright:  (c) 2017 zhihu
:authors: hanxinyu<hanxinyu@zhihu.com>
:version: 1.0 of 2017-09-21
'''

import exception
from commander import CommandManager


def main():
    '''入口函数
    '''
    while True:
        input_str = raw_input('输入想要的命令，帮助命令为help\n>>')

        try:
            CommandManager.execute(input_str)
        except exception.QuitException:
            break
        except exception.CommandNotFoundException:
            print '未找到对应命令'


if __name__ == "__main__":
    main()
