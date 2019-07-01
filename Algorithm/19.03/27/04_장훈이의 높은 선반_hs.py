def tower(start, n):
    global li_tower
    global temp, result

    if n == 0:
        return

    for i in range(start, N):
        li_tower.append(i)
        temp += li_H[i]
        if temp < result:
            if temp < B:
                tower(i + 1, n - 1)
            else:
                if result > temp:
                    result = temp
        temp -= li_H[i]
        li_tower.remove(i)


T = int(input())

for t in range(T):
    N, B = map(int, input().split())
    li_H = list(map(int, input().split()))

    result = 200001
    temp = 0
    li_tower = []

    tower(0, N)
    print("#{} {}".format(t + 1, result-B))