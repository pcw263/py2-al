#!/usr/bin/env python2
#-*- coding:utf-8 -*-

class Stack(object):
    def __init__(self):
        self.__items__ = [] 

    def isEmpty(self):
        return self.__items__ == []

    def push(self,item):
        self.__items__.append(item)

    def peek(self):
        return self.__items__[-1]

    def pop(self):
        return self.__items__.pop()

    def size(self):
        return len(self.__items__)

