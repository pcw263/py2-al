#!/usr/bin/env python2
#-*- coding:utf-8 -*-

from stack import Stack

def convert(num, obj_type):
    #十进制转换为其他进制—obj
    dights = "0123456789ABCDEF"
    new = Stack()
    obj = int(obj_type)
    while num > 0:
        rest = num % obj
        new.push(rest)
        num = num // obj
        
    num_obj = ""
    while not new.isEmpty():
        num_obj += dights[new.pop()]

    return num_obj

if __name__ == "__main__":
    import sys
    obj_set = set(["2","8","10","16"])
    try:
        base_num = int(sys.argv[1].strip())
    except:
        raise Exception("plz input dec_number!")
    obj_type = sys.argv[2].strip()
    if obj_type not in obj_set:
        raise Exception("plz input the right target type!")

    print base_num, "--------->",\
            convert(base_num, obj_type)

    
