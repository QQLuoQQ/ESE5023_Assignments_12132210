# -*- coding: utf-8 -*-
"""
Created on Mon Oct  4 17:44:23 2021

@author: LQQ
"""

######I got inspired by reading https://www.jianshu.com/p/47c293171764
def Pascal_triangle(k):
    row = [1]
    for _ in range(k):
        row = [x+y for x, y in zip([0] + row, row+[0])]##can't really understand
    return row
print(Pascal_triangle(5))
#print(Pascal_triangle(100))
#print(Pascal_triangle(200))
