from math import sqrt
data = input().split()
points_a = [ float(i) for i in data ]
data = input().split()
points_b = [ float(k) for k in data ]
print('{:.4f}'.format(sqrt( (points_b[0] - points_a[0])**2 + (points_b[1] - points_a[1])**2 )))
