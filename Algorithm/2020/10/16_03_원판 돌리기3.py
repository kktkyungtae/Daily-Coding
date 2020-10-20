# https://www.acmicpc.net/problem/17822

# 1. 원판 숫자의 총합을 nsum에 저장하고 개수를 nm에 저장한다
# 2. k를 m으로 나눈 나머지를 기준으로 원판 배열을 회전하고 방문 체크 배열 c도 같이 회전한다
# 3. 방문하지 않았던 숫자에 대해서 bfs를 수행한다
# 4. bfs로 이동하면서 y가 0보다 작으면 m-1, m-1보다 크면 0으로 바꿔서 원을 이루도록 한다
# 5. 다음 칸의 숫자가 같으면 체크하고 몇 개가 같은지 세는 xnct를 증가시킨다
# 6. return 값이 있으면 지운 숫자의 합만큼 nsum에서 빼주고 nm도 빼준다
#    지운 숫자가 있음을 알려주는 flag를 1로 저장한다
# 7. 만약 모든 숫자를 지웠으면 0을 출력하고 끝낸다
#    평균을 계산할 때 0으로 나누는 것을 방지할 수 있다
# 8. 지운 숫자가 없으면 문제의 조건대로 숫자를 바꾸고 nsum도 같이 빼거나 더해준다
# 9. 마지막에 nsum을 출력한다

from collections import deque
import sys
input = sys.stdin.readline
n, m, t = map(int, input().split())

# 총 수의 합, 총 숫자의 갯수
total, ns = 0, n*m
wonpan = []
for _ in range(n):
    row = deque(map(int, input().split()))
    # row = list(map(int, input().split()))
    wonpan.append(row)
    total += sum(row)

q = deque()
vst = [[0]*m for _ in range(n)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(x, y):
    q.append([x, y])
    # 다음 숫자가 같으면, 몇개 같은지 체크하는
    check_n = 0
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # y가 0보다 작으면, m - 1 / y가 m - 1 보다 크면 0으로 바꿔서 원으로 만들어
            if ny < 0:
                ny = m - 1
            elif ny > m - 1:
                ny = 0

            if 0 <= nx < n and 0 <= ny < m and vst[nx][ny] == 0:
                if wonpan[x][y] == wonpan[nx][ny]:
                    vst[nx][ny] = 1
                    q.append([nx, ny])
                    check_n += 1

    return check_n

for _ in range(t):
    x, d, k = map(int, input().split())

    # 요거는 배열 돌리기..
    k %= m
    for i in range(x-1, n, x):
        if d == 0:
            wonpan[i] = wonpan[i][-k:] + wonpan[i][:-k]
            vst[i] = vst[i][-k:] + vst[i][:-k]
        else:
            wonpan[i] = wonpan[i][k:] + wonpan[i][:k]
            vst[i] = vst[i][k:] + vst[i][:k]

    # # 요거는 rotate
    # for i in range(n):
    #     if (i + 1) % x == 0:
    #         if d == 0:
    #             wonpan[i].rotate(k)
    #         else:
    #             wonpan[i].rotate(-k)

    flag = 0
    for i in range(n):
        for j in range(m):
            if vst[i][j] == 0:
                c_n = bfs(i, j)
                # 같은 수가 있으면
                if c_n != 0:
                    # 지운 숫자의 합 만큼 빼준다
                    total -= wonpan[i][j] * c_n
                    ns -= c_n
                    # 지운수가 있는 것을 나타내는 flag = 1
                    flag = 1

    # 만약 원판의 모든 수를 지웠다면,
    if ns == 0:
        print(0)
        sys.exit()

    # 지워진 게 없다면
    if flag == 0:
        avg = total / ns
        for i in range(n):
            for j in range(m):
                if vst[i][j] == 0:
                    # 평균보다 크면 -1
                    if wonpan[i][j] > avg:
                        wonpan[i][j] -= 1
                        total -= 1
                    elif wonpan[i][j] < avg:
                        wonpan[i][j] += 1
                        total += 1

print(total)
