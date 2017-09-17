#!/usr/bin/env python2
#-*- coding:utf-8 -*-

def insert_sort(unorder_list):
    for insert_num in range(1,len(unorder_list)+1):
        #insert_obj = unorder_list[num]
        #for pos in range(part-1,0,-1):
        pos = insert_num-1
        stop = False
        while pos>=0 and not stop:
            if unorder_list[pos]<unorder_list[insert_num]:
                #unorder_list.insert(pos,insert_num)
                unorder_list[pos],unorder_list[insert_num] = \
                unorder_list[insert_num],unorder_list[pos]
                stop = True
            pos -= 1

if __name__ == "__main__":
    test_list = [12,432,435,674,23,49,69,83,123]
    insert_sort(test_list)
    print test_list