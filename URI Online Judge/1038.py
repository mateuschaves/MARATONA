prices = [None, 4, 4.5, 5, 2, 1.5]
data = [ int(i) for i in input().split() ]
c, q = data
print('Total: R$ {:.2f}'.format( prices[c] * q ))
