def rotate(r, c, s):
    for i in range(1, s + 1):
        temp = data[r - i][c - i]

        # 세로 - 위로
        for j in range(r - i, r + i):
            data[j][c - i] = data[j + 1][c - i]

        # 세로 - 아래로
        for k in range(r + i, r - i, -1):
            data[k][c + i] = data[k - 1][c + i]

        for h in range(c - i, c + i):
            data[r + i][h] = data[r + i][h + 1]

        for l in range(c + i, c - i, -1):
            data[r - i][l] = data[r - i][l - 1]

        data[r - i][c - i + 1] = temp


def reverse_rotate(r, c, s):
    for i in range(1, s + 1):
        temp = data[r - i][c - i]

        for j in range(c - i, c + i):
            data[r - i][j] = data[r - i][j + 1]

        for j in range(r - i, r + i):
            data[j][c + i] = data[j + 1][c + i]

        for j in range(c + i, c - i, -1):
            data[r + i][j] = data[r + i][j - 1]

        for j in range(r + i, r - i, -1):
            data[j][c - i] = data[j - 1][c - i]

        data[r - i + 1][c - i] = temp


def check():
    global ans
    for i in data:
        temp = sum(i)
        if ans > temp:
            ans = temp


def sol(cnt):
    if cnt == K:
        check()
        return
    for i in range(K):
        if visit[i]:
            rotate(rcs[i][0], rcs[i][1], rcs[i][2])
            visit[i] = False
            sol(cnt + 1)
            visit[i] = True
            reverse_rotate(rcs[i][0], rcs[i][1], rcs[i][2])


N, M, K = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(N)]
rcs = [list(map(int, input().split())) for _ in range(K)]
visit = [True] * K
for _ in range(K):
    rcs[_][0] -= 1
    rcs[_][1] -= 1
ans = 2 << 30
sol(0)
print(ans)

'''
5 6 2
1 2 3 2 5 6
3 8 7 2 1 3
8 2 3 1 4 5
3 4 5 1 1 1
9 3 2 1 4 3
3 4 2
4 2 1

'''