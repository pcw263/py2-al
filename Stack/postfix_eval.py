#!/usr/bin/env python2
#-*- coding:utf-8 -*-

from stack import Stack

def math_op(op,obj1,obj2):
    if op == "+":
        return obj1+obj2
    elif op == "-":
        return obj1-obj2
    elif op == "*":
        return obj1*obj2
    else:
        return obj1/obj2

def postfix_eval(postfix_str):
    #postfix中的符号按照空格分割
    token_list = postfix_str.split(" ")
    post_stack = Stack()

    for token in token_list:
        if token in "0123456789":
            post_stack.push(int(token))
        else:
            obj1 = post_stack.pop()
            obj2 = post_stack.pop()
            op_obj = math_op(token,obj2,obj1)
            post_stack.push(op_obj)
    return post_stack.pop()

if __name__ : "__main__":
    import sys
    postfix = sys.stdin.readline().strip()
    print postfix_eval(postfix)
