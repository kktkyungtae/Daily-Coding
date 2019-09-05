# SW Expert Academy
# https://swexpertacademy.com/main/learn/course/lectureProblemViewer.do

# 2차원 평면에 원자들이 주어진다
# 원자는 위치 / 방향 / 크기가 있다
# 원자가 부딪히면서 가지고 있는 크기만 큼 에너지 방출한다
# 에너지의 총합을 구해라

# 이동방향 0 : 상, 1 : 하, 2 : 좌, 3 : 우
# 원자들의 이동 범위의 제한은 없다
# 원자들의 이동 방향은 바뀌지 않는다
# 원자는 부딪히면 에너지 방출하고 바로 소멸

tc = int(input())

def check():
    pass

for t in range(tc):
    n = int(input())
    mapp = [list(map(int, input().split())) for _ in range(n)]

    # x, y, dir, e
    # mapp = [[0]*1001 for _ in range(1001)]
    # for i in range(n):
    #     x, y, dir, e = map(int, input().split())
    #     mapp[x, y] = [dir, e]

    direction = [(0, 0.5), (0, -0.5), (-0.5, 0), (0.5, 0)]

    if len(mapp) < 2:
        break
    else:
        for i in range(len(mapp)):



