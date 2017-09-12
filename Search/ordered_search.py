#!/usr/bin/env python2
#-*- coding:utf-8 -*-

def ordered_search(test_list, search_obj):
    found = False
    stop = False
    pos = 0

    while pos < len(test_list) and not found and not stop:
        if test_list[pos] == search_obj:
            found = True
        else:
            if test_list[pos] > search_obj:
                stop = True
            else:
                pos += 1

    return found

if __name__ == "__main__":
    test_list = [1,3,5,8,11,15,18,26,38,51,63]
    print ordered_search(test_list, 17)