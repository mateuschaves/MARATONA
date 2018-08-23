data = input().split()
data = [ int(i) for i in data ]
a, b, c = data
mab = (a + b + abs(a - b)) // 2
mxc = (mab + c + abs(mab - c)) // 2
print('{} eh o maior'.format(mxc))
