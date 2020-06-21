# -*- coding: utf-8 -*-

data = input()
data = [ float(i) for i in data.split() ]
a, b, c = data
delta = (b ** 2) - (4*a*c)
if a == 0 or delta < 0:
    print('Impossivel calcular')
else:
    print('R1 = {:.5f}'.format(( ((-b) + delta ** (1/2)) / (2 * a) )))
    print('R2 = {:.5f}'.format(( ((-b) - delta ** (1/2)) / (2 * a) )))
