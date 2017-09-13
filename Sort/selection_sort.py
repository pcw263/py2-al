#!/usr/bin/env python2
#-*- coding:utf-8 -*-

def selection_sort(unorder_list):
    for epoch in range(len(unorder_list)-1,0,-1):
        pos_of_max = 0
        for pos in range(1,epoch+1):
            if unorder_list[pos] > unorder_list[pos_of_max]:
                pos_of_max = pos

        unorder_list[epoch],unorder_list[pos_of_max] = unorder_list[pos_of_max],unorder_list[epoch]

if __name__ == "__main__":
    list1 = [12,432,435,674,23,49,69,83,123]
    selection_sort(list1)
    print list1