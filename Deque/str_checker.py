#!/usr/bin/env python2
#-*- coding:utf-8 -*-

from deque import Deque

def checker(obj_str):
    checker_deque = Deque()
    equal = True

    for char in obj_str:
        checker_deque.addRear(char)

    while checker_deque.size() > 1 and equal:
        first = checker_deque.removeFront()
        last = checker_deque.removeRear()
        if first != last:
            equal = False

    return equal

if __name__ == "__main__":
    test_str = "queuq"
    print checker(test_str)
    
