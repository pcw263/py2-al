#!/usr/bin/env python2
#-*- coding:utf-8 -*-

import sys
sys.path.append("../Stack/")
from stack import Stack

def num2str(num_str,base):
    num = int(num_str)
    str_ = "0123456789ABCDEF"
    str_stack = Stack()

    while num > 0:
        if num < base:
            str_stack.push(str_[num])
        else:
            str_stack.push(str_[num % base])
        num = num // base
        #str_stack.push(rest)

    target_str = ""
    while not str_stack.isEmpty():
            target_str += str_stack.pop()

    return target_str

if __name__ == "__main__":
    num = sys.argv[1].strip()
    print num
    bin_str = num2str(num,2)
    print bin_str

