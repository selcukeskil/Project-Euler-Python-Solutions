# -*- coding: utf-8 -*-
"""
Created on Thu Oct 28 21:47:49 2021

@author: selcu
"""


a=0
for i in range(1,1000):
    if i%3 ==0 or i%5==0:
        a+=i
print(a)
        