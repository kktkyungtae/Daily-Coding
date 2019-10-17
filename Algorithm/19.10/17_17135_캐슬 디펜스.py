# Baekjoon
# https://www.acmicpc.net/problem/17135

# 2차 배열의 적들이 몰려오는데
# 3명의 궁수를 배치해서 적을 죽여야한다
# 2차 배열에 마지막행에 한 칸을 추가해서 궁수를 배치하고
# 최대로 죽일 수 있는 적의 수를 출력해라

# 거리가 가까운적 부터 죽이고, 거리가 같으면 왼쪽 부터

import itertools

def deepcopy(arr):
    return [i[:] for i in arr][:]


def kill(x, y, z, map):
    map = map + [[0] * n]
    map[n][x] = 2
    map[n][y] = 2
    map[n][z] = 2







n, m, d = map(int, input().split())
mapp = [list(map(int, input().split())) for _ in range(n)]

location = list(range(n))
attack = list(itertools.combinations(location, 3))

ans = 0
for i in range(len(attack)):
    a, b, c = attack[0], attack[1], attack[2]
    kill(a, b, c, mapp)


'''

5 5 1
0 0 0 0 0
0 0 0 0 0
0 0 0 0 0
0 0 0 0 0
1 1 1 1 1

'''