#!/usr/bin/env python2
#-*- coding:utf-8 -*-

def binary_search(test_list, target):
    found = False
    #pos = len(test_list)//2
    #stop = False

    '''
    #这样做改变test_list本身并不好，会使得search之后会使得原始列表改变
    #这样看来pos的设置也使得条件判断更麻烦了
    while not found and not stop:
        if test_list[pos] == target:
            found = True
        elif len(test_list)>1:
            if test_list[pos] > target:
                test_list = test_list[:pos]
            else:
                test_list = test_list[pos:]

            pos = len(test_list)//2
        else:
            stop = True
    '''

    first = 0
    last = len(test_list) - 1
    while not found and first<=last:
        mid = (first+last)//2
        if test_list[mid] == target:
            found =True
        else:
            if test_list[mid] > target:
                last = mid - 1
            else:
                first = mid + 1

    return found

'''
用递归的方式实现二分
'''
def bin_search_rec(test_list,target):
    first = 0
    last = len(test_list)-1
    #while not found and last >= first:
    #基本终止条件 list is null,不需要while循环了
    if len(test_list) == 0:
        return False
    else:
        mid = len(test_list)//2
        if test_list[mid] == target:
            return True
        else:
            if test_list[mid] > target:
                return bin_search_rec(test_list[:mid],target)
            else:
                return bin_search_rec(test_list[mid+1:],target)


if __name__ == "__main__":
    test_list = [1,5,9,15,19,24,28,37,46,51,58,63,79,88,93]
    print test_list
    print 8,"--->",binary_search(test_list, 8)
    print 88,"--->",binary_search(test_list, 88)