# -*- coding: utf-8 -*-
"""
Created on Fri Dec 17 23:26:27 2021

@author: selcu
"""
sumOfSquares = 0
squareOfSums = 0
for i in range(1,101):
    squareOfSums += i 
    sumOfSquares += i**2
    
print(squareOfSums**2-sumOfSquares)

