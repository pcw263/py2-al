#!/usr/bin/env python2
#-*- coding:utf-8 -*-

from stack import Stack

# {[((()))]()}

def matcher(op,cl):
    opens = "{[("
    closes = "}])"
    return opens.index(op) == closes.index(cl)

def symbol_match(symbol_str):
    s = Stack()
    pos = 0
    matched = True

    while pos < len(symbol_str) and matched:
        symbol = symbol_str[pos]
        if symbol in "{[(":
            s.push(symbol)
        else:
            if s.isEmpty():
                matched = False
            else:
                top = s.pop()
                if not matcher(top,symbol):
                    matched = False
        pos += 1

    if matched and s.isEmpty():
        return True
    else:
        return False

if __name__ == "__main__":
    import sys
    line = sys.stdin.readline().strip("\n")
    #print line
    print symbol_match(line)


