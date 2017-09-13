#!/usr/bin/env python2
#-*- coding:utf-8 -*-
import time

def bubble_sort(unorder_list):
    #start = time.time()
    count = 0
    for epoch in range(len(unorder_list)-1,0,-1):
        '''
        这里迭代器是从大到小地生成序列（9，8，7，.....,1）
        如：range(3,0,-1) ------> 依次生成 3，2，1  (注意递减生成时不包括最后一项)
        '''
        for i in range(epoch):     #已经将前(n-epoch)个最大的数字”冒泡“到其应在的位置上
            if unorder_list[i] > unorder_list[i+1]:
                unorder_list[i],unorder_list[i+1] = unorder_list[i+1],unorder_list[i]
        count += 1
    #end = time.time()
    print "冒泡操作数：",count
    #return unorder_list

def short_bubble_sort(unorder_list):
    #start = time.time()
    count = 0
    change = True
    num = len(unorder_list)-1
    while num > 0 and change:
        change = False 
        #for epoch in range(num,0,-1):
        for i in range(num):
            if unorder_list[i] > unorder_list[i+1]:
                change = True
                unorder_list[i],unorder_list[i+1] = unorder_list[i+1],unorder_list[i]
        count += 1
        num -= 1
    #end = time.time()
    print "冒泡操作数：",count

if __name__ == "__main__":
    unorder1 = [1,3,5,6,8,9,15,55,36,28,99,77,88]
    unorder2 = [1,3,5,6,8,9,15,55,36,28,99,77,88]
    bubble_sort(unorder1)  #sort
    short_bubble_sort(unorder2)
    print "1:", unorder1
    print "2:", unorder2