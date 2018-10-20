n = int(input())

i = 0
while True:
    if i == 6:
        break
    if n % 2 != 0:
        i = i + 1
        print(n)
    n = n + 1
