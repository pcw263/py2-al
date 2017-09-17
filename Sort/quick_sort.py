#!/usr/bin/env python2
#-*- coding:utf-8 -*-

def quick_sort(alist):
    quicksort_helper(alist, 0, len(alist)-1)

def quicksort_helper(alist,first,last):
    if last > first:
        splitpoint = partition(alist, first, last)

        quicksort_helper(alist, first, splitpoint-1)
        quicksort_helper(alist, splitpoint+1, last)

def partition(alist,first,last):
    leftmark = first+1
    rightmark = last

    done = False
    #while leftmark < rightmark:
    while not done:
        while leftmark <= rightmark and alist[leftmark] <= alist[first]:
            leftmark += 1

        while rightmark >= leftmark and alist[rightmark] >= alist[first]:
            rightmark -= 1

        if rightmark < leftmark:
            done = True
        else:
            alist[leftmark],alist[rightmark] = alist[rightmark],alist[leftmark]

    #最后将枢轴值放置到分裂点
    alist[first],alist[rightmark] = alist[rightmark],alist[first]

    return rightmark

alist = [13,45,26,75,49,88,33,66,11,22,55,44]
quick_sort(alist)
print alist

        