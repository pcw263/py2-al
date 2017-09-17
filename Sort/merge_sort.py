#!/usr/bin/env python2
#-*- coding:utf-8 -*-

'''
merge sort n*O(logn)
'''

def mergeSort(alist): 
    print("Splitting ",alist)
    if len(alist)>1:
        mid = len(alist)//2 
        lefthalf = alist[:mid] 
        righthalf = alist[mid:]

        mergeSort(lefthalf) 
        mergeSort(righthalf)
        #print lefthalf
        #print righthalf
        i=0
        j=0
        k=0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]: 
                alist[k]=lefthalf[i] 
                i=i+1
            else: 
                alist[k]=righthalf[j] 
                j=j+1
            k=k+1
        while i < len(lefthalf): 
            alist[k]=lefthalf[i] 
            i=i+1
            k=k+1
        while j < len(righthalf): 
            alist[k]=righthalf[j] 
            j=j+1
            k=k+1
    print("Merging ",alist)



alist = [1,2,3,4,5,6,7,8,9]
mergeSort(alist)