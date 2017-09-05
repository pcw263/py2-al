#!/usr/bin/env python2
#-*- coding:utf-8 -*-

def ListSum(list_):
    #使用递归对列表内的数字求和
    if len(list_) == 1:
        return list_[0]
    
    else:
        return list_[0] + ListSum(list_[1:])

if __name__ == "__main__":
    test_list = [1,2,3,4,5]
    print test_list
    print ListSum(test_list)
