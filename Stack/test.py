#!/usr/bin/env python2
#-*- coding:utf-8 -*-

from stack import Stack

if __name__ == "__main__":
    s = Stack()
    print s.isEmpty()

    #push
    s.push(0)
    s.push("Hi")
    s.push("~")

    print s.size()
    #peek
    print s.peek()
    
    #pop
    s.pop()
    print s.peek()
