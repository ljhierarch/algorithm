# -*- coding: utf-8 -*-

'''
commander
~~~~~~~~~~~~

命令模块，集中交互命令处理

:copyright:  (c) 2017 zhihu
:authors: hanxinyu<hanxinyu@zhihu.com>
:version: 1.0 of 2017-09-21
'''

import exception
from warehouse import keeper


class CommandManager(object):
    '''命令管理
    '''

    __instance = None

    def __init__(self):
        '''初始化方法
        '''
        self.commanders = {}

    @classmethod
    def get_manager(cls):
        '''获取管理员
        '''
        if not CommandManager.__instance:
            CommandManager.__instance = CommandManager()

        return CommandManager.__instance

    @classmethod
    def get_commander(cls, command):
        '''获取命令执行

        Args:
            command: 命令名称
        Returns:
            返回命令执行方法
        '''
        return cls.get_manager().commanders.get(command)

    @classmethod
    def manager_commander(cls, commander):
        '''管理命令

        Args:
            commander: 命令处理人
        '''
        cls.get_manager().commanders[commander.name] = commander

    @staticmethod
    def command_pre_treat(command):
        '''指令预处理
        '''
        actions = command.split(' ')
        return [action.strip() for action in actions if action]

    @classmethod
    def execute(cls, input_str):
        '''执行命令
        '''
        actions = cls.command_pre_treat(input_str)
        commander = cls.get_commander(actions[0])
        if not commander:
            raise exception.CommandNotFoundException('未找到命令')

        commander.execute(actions)


class CommanderMeta(type):
    '''命令元类，命令类构建的时候调用，用于将命令类纳入到命令管理者的管理之中
    '''

    def __new__(meta, name, bases, dct):
        '''产生类实例
        '''
        return super(CommanderMeta, meta).__new__(meta, name, bases, dct)

    def __init__(cls, name, bases, dct):
        '''构建类实例
        '''
        super(CommanderMeta, cls).__init__(name, bases, dct)
        CommandManager.manager_commander(cls)


# 命令基类
class Commander(object):
    '''命令
    '''

    name = 'origin'
    __metaclass__ = CommanderMeta

    @classmethod
    def execute(cls, commands):
        '''命令处理
        '''
        raise NotImplementedError

    @classmethod
    def self_introduct(cls):
        '''自我介绍
        '''
        with open('./docs/{}.txt'.format(cls.name)) as des_doc:
            print des_doc.read()


# help命令
class HelpCommander(Commander):
    '''帮助命令
    '''

    name = 'help'

    @classmethod
    def execute(cls, commands):
        '''帮助命令
        '''
        if not commands:
            print '未接收到命令信息'

        if len(commands) == 1:
            cls.self_introduct()
            return

        commander = CommandManager.get_commander(commands[1])
        if commander:
            commander.self_introduct()
            return

        algorithm = keeper.get_algorithm(commands[1])
        if algorithm:
            algorithm.self_introduct()
            return

        print '未找到要帮助的命令或者算法'


# quit命令
class QuitCommander(Commander):
    '''退出命令
    '''

    name = 'quit'

    @classmethod
    def execute(cls, commands):
        '''退出命令
        '''
        raise exception.QuitException('退出')


# execute命令
class Execute(Commander):
    '''执行算法
    '''

    name = 'execute'

    @classmethod
    def execute(cls, commands):
        '''执行算法
        '''

        algorithm = keeper.get_algorithm(commands[1])
        if not algorithm:
            print '未找到对应算法，请在仓库文件下查看，算法名称和算法实现对应文件名相同'
            return
        algorithm().execute()
