#!/usr/bin/env python2
#-*- coding:utf-8 -*-

from stack import Stack

def postfix(op_str):
    #定义字典，用于保存操作符的优先级
    prec = {}
    prec["*"] = 3
    prec["/"] = 3
    prec["+"] = 2
    prec["-"] = 2
    prec["("] = 1
    #实例化一个栈，以及一个输出符号的存储列表
    opstack = Stack()
    postfix_list = []
    obj_list = list(op_str)

    for token in obj_list:
        #如果是操作数
        if token in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or token in "1234567890":
            postfix_list.append(token)
        #如果是括号（局部运算的起始/终止）
        elif token == "(":
            opstack.push(token)
        
        elif token == ")":
            top_token = opstack.pop()
            while top_token != "(":
                postfix_list.append(top_token)
                top_token = opstack.pop()
        #如果是操作符
        else:
            while (not opstack.isEmpty()) and (prec[opstack.peek()] >= prec[token]):
                postfix_list.append(opstack.pop())
            opstack.push(token)

    while not opstack.isEmpty():
        postfix_list.append(opstack.pop())

    return " ".join(postfix_list)

if __name__ == "__main__":
    import sys
    op_str = sys.stdin.readline().strip()
    
    print postfix(op_str)


