#!/usr/bin/env python2
#-*- coding:utf-8 -*-
class HashTable(object):
    def __init__(self):
        self.size = 11
        self.key = [None]*self.size
        self.value = [None]*self.size

    