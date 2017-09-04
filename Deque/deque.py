#!/usr/bin/env python2
#-*- coding:utf-8 -*-

class Deque(object):
    '''
    双端队列：
    支持队列两端的添加/删除操作
    '''
    def __init__(self):
        self.__deque__ = []

    def addFront(self,item):
        #这里定义list_index=0的位置为尾部（底部）
        #所以这里的Front是对队首进行添加
        self.__deque__.append(item)

    def addRear(self,item):
        self.__deque__.insert(0,item)

    def removeFront(self):
        return self.__deque__.pop()

    def removeRear(self):
        return self.__deque__.pop(0)
    #从队首添加/删除是O(1)的，而从队尾进行操作是O(n)的；
    #n为队列长度

    def isEmpty(self):
        return self.__deque__ == []

    def size(self):
        return len(self.__deque__)
