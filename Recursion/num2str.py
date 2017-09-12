#!/usr/bin/env python2
#-*- coding:utf-8 -*-

def num2str(num,base):
    strs = "0123456789"

    if num < base:
        return strs[num]

    else:
        return num2str(num//base,base) + strs[num%base]

if __name__ == "__main__":
    n = 438
    n_ = num2str(438,10)
    print n ,type(n)
    print n_,type(n_)
