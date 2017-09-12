#!/usr/bin/env python2
#-*- coding:utf-8 -*-

import turtle

myturtle = turtle.Turtle()
mywindow = turtle.Screen()

def test_draw(myturtle, linelen):

    if linelen > 0:
        myturtle.forward(linelen)
        myturtle.right(90)
        test_draw(myturtle, linelen-5)

test_draw(myturtle, 100)
mywindow.exitonclick()