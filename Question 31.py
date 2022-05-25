# -*- coding: utf-8 -*-


wayCounter = 0

a = 1
b = 2
c = 5
d = 10
e = 20
f = 50 
g = 100
h = 200

for i in range(201):
    for j in range(101):
        for k in range(41):
            for l in range(21):
                for m in range(11):
                    for n in range(5):
                        for o in range(3):
                            for p in range(2):
                                if a*i + b*j + c*k + d*l + e*m +f*n+g*o+h*p==200:
                                    wayCounter+=1
                                    print(wayCounter)
                                    
print(wayCounter)
