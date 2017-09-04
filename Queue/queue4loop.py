#!/usr/bin/env python2
#-*- coding:utf-8 -*-

from queue import Queue

def queue4loop(cond_list,count):
    queue = Queue()
    for item in cond_list:
        queue.enqueue(item)

    while queue.size() > 1:
        for i in range(count):
            queue.enqueue(queue.dequeue())
        
        queue.dequeue()

    return queue.dequeue()

if __name__ == "__main__":
    condidate = ["A","B","C","D","E"]
    print queue4loop(condidate,3)
