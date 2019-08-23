from sys import stdin
quee = []
for _ in range(int(stdin.readline())):
    arr = stdin.readline().split()
    if arr[0] == 'push':
        quee.append(arr[1])
    elif arr[0] == 'pop':
        if quee:
            print(quee.pop(0))
        else:
            print(-1)
    elif arr[0] == 'size':
        print(len(quee))
    elif arr[0] == 'empty':
        if len(quee) == 0:
            print(1)
        else:
            print(0)
    elif arr[0] == 'front':
        if quee:
            print(quee[0])
        else:
            print(-1)
    elif arr[0] == 'back':
        if quee:
            print(quee[-1])
        else:
            print(-1)
    else:
        pass
