n = int(input())
for k in range(n):
    data = input().split()
    a = data[0]
    b = data[1]
    c = a.rfind(b)
    if len(b) > len(a):
        print('nao encaixa')
    elif c + len(b) == len(a):
        print('encaixa')
    else:
        print('nao encaixa')
    # A quantidade de casas contando da ultima posíção
    # até a primeira ocorrência precisa ser igual ao
    # cumprimento  da segunda string.
