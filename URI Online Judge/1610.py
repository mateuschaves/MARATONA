iv = [
'3',
'2 1',
'1 2',
'2 2',
'1 2',
'2 1',
'4 4',
'2 3',
'3 4',
'4 2',
'1 3',
]
input = lambda: iv.pop(0)


cases = int(input())

for _ in range(cases):
    n, m = [ int(i) for i in input().split() ]

    graph = [ False for i in range(n + 1) ]

    loop = False

    for _ in range(m):
        doc, dep = [ int(i) for i in input().split() ]
        if graph[dep]:
            loop = True
            break
        else:
            graph[doc] = True

    print('SIM' if loop else 'NAO')

