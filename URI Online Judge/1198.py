while True:
    try:
        data = input().split()
        data = [int(i) for i in data]
        print(abs(data[1] - data[0]))
    except EOFError:
        break
