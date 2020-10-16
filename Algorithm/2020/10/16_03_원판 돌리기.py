from collections import deque

n, m, t = map(int, input().split())
maps = [[0 for _ in range(n)]]
for _ in range(n):
    tmp = deque(map(int, input().split()))
    maps.append(tmp)

spin = deque()
for _ in range(t):
    spin.append(list(map(int, input().split())))

def bfs():
    pass


# 돌면서 같은거 있으면 지우고, 없으면 평균 때려
def clear():
    pass


# 행렬 돌려놔
while spin:
    x, d, k = spin.popleft()
    for i in range(1, len(maps)):
        if i % x == 0:
            # 시계 방향
            if d == 0:
                maps[i].rotate(k)

            # 반시계 방향
            else:
                maps[i].rotate(-k)

    clear()


