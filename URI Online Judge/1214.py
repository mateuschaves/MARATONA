n = int(input())
for i in range(n):
    students = 0
    average = 0
    data = input().split()
    data = [ int(i) for i in data ]
    for pos, j in enumerate(data):
        if pos != 0:
            average += data[pos]
    average = average / (len(data) - 1)
    for pos, k in enumerate(data):
        if pos != 0 and k > average:
            students += 1
    print('{:.3f}%'.format( 100 * students / (len(data) - 1) ))



