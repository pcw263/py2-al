#!/usr/bin/env python2
#-*- coding:utf-8 -*-

class Queue(object):
    '''
    定义队列数据类型，基本为：
    操作队尾添加项，队首移除项
    '''
    def __init__(self):
        self.__queue__ = []

    def isEmpty(self):
        return self.__queue__ == []

    def enqueue(self,item):
        self.__queue__.insert(0,item)
        #self.__queue__ = [item] + self.__queue__

    def dequeue(self):
        #这里返回弹出的队首对象
        return self.__queue__.pop()

    def size(self):
        return len(self.__queue__)
