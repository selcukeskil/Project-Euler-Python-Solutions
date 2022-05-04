# -*- coding: utf-8 -*-
"""
Created on Thu Oct 28 21:57:14 2021

@author: selcu
"""
toplam=0
a=1
b=1
for i in range(100):
    c=a+b
    print(c)
    if c%2==0 and c<4000000:
        toplam+=c
    a=b
    b=c
    
print("Toplam = ", toplam)
