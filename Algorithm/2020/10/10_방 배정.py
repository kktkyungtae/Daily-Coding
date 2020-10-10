n, s = map(int, input().split())
clas = [[0,0] for _ in range(6)]

for i in range(n):
    a, b = map(int, input().split())
    if b == 1:
        if a == 0:
            clas[0][0] += 1
        else:
            clas[0][1] += 1
    elif b == 2:
        if a == 0:
            clas[1][0] += 1
        else:
            clas[1][1] += 1
    elif b == 3:
        if a == 0:
            clas[2][0] += 1
        else:
            clas[2][1] += 1
    elif b == 4:
        if a == 0:
            clas[3][0] += 1
        else:
            clas[3][1] += 1
    elif b == 5:
        if a == 0:
            clas[4][0] += 1
        else:
            clas[4][1] += 1
    else:
        if a == 0:
            clas[5][0] += 1
        else:
            clas[5][1] += 1

count = 0
for l in range(6):
    for h in range(2):
        if clas[l][h] % s == 0:
            count += clas[l][h] // s
        else:
            count += (clas[l][h] // s) + 1

print(count)

# [[1, 2], [2, 1], [1, 3], [0, 1], [1, 2], [1, 1]]
# # 11

# [[2, 1], [1, 2], [3, 1], [1, 0], [2, 1], [1, 1]]
# 12