# -*- coding: utf-8 -*-


sumOfSquares = 0
squareOfSums = 0
for i in range(1,101):
    squareOfSums += i 
    sumOfSquares += i**2
    
print(squareOfSums**2-sumOfSquares)

