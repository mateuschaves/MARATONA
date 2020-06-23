# -*- coding: utf-8 -*-

data = [ int(i) for i in input().split() ]

a, b, c, d = data

if b > c and d > a and c + d > a + b and c > 0 and d > 0 and a % 2 == 0:
    print("Valores aceitos")
else:
    print("Valores nao aceitos")



