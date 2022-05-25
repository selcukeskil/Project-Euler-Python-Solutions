# -*- coding: utf-8 -*-


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
