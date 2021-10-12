# -*- coding: utf-8 -*-
"""
Created on Mon Sep 27 23:39:37 2021

@author: LQQ
"""
def Print_values(a,b,c):
    if a>b:
        if b>c:
            print("a=%d,b=%d,c=%d" % (a, b, c))
        elif a>c:
            print("a=%d,c=%d,b=%d"%(a,c,b))
        else:
            print("c=%d,a=%d,b=%d"%(c,a,b))
    elif b>c:
        print('stop')
        # break
    else:
        print("c=%d,b=%d,a=%d"%(c,b,a))
     
Print_values(6,4,3)
