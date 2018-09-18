import math

data = input()
data = [ float(i) for i in data.split() ]
a, b, c = data
delta = pow(b, 2) - (4*a*c)
if a == 0 or delta < 0:
    print('Impossivel calcular')
else:
    print('R1 = {}'.format(( (-b) + math.sqrt(delta)) / 2 * a ))
    print('R2 = {}'.format(( (-b) - math.sqrt(delta)) / 2 * a ))
