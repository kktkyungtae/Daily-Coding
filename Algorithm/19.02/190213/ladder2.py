import sys
sys.stdin= open("ladder.txt","r")

for i in range(10):
    t = int(input())
    a = [[0] * 100 for _ in range(100)]

    for i in range(100):
        a[i] = list(map(int, input().split()))

    x = y = 0

    for i in range(100):
        for j in range(100):
            if (a[i][j] == 2):
                x = i
                y = j

    while (x > 0):
        if (y == 0):
            if (a[x][y + 1] == 1):
                a[x][0] = 0
                y = y + 1
            else:
                x = x - 1
            continue
        if (y == 99):
            if (a[x][y - 1] == 1):
                a[x][99] = 0
                y = y - 1
            else:
                x = x - 1
            continue

        if (a[x][y - 1] == 1):
            a[x][y] = 0
            y = y - 1

        if (a[x - 1][y] == 1):
            a[x][y] = 0
            x = x - 1

        if (a[x][y + 1] == 1):
            a[x][y] = 0
            y = y + 1

    if (x == 0): print(f"#{t} {y}")