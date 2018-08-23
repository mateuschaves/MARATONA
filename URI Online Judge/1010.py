p1 = input().split()
p1 = [float(i) for i in p1]
p2 = input().split()
p2 = [float(i) for i in p2]

print('VALOR A PAGAR: R$ {:.2f}'.format( (p1[1] * p1[2]) + (p2[1] * p2[2])))
