s = int(input())
h = s // 3600
m = s % 3600 // 60
ss = s - ( h * 3600) - (m * 60)
print('{}:{}:{}'.format(h, m ,ss))
