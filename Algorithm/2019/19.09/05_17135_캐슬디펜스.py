# 백준
# https://www.acmicpc.net/problem/17135

<<<<<<< HEAD
# NxM 격자 판에 성으로 몰려오는 적들이 있다
# N+1 마지막 칸에 성이 있고 / 궁수 세명이 있는데
# 궁수는 적을 공격해서 죽인다

# 모든 궁수는 적을 동시에 공격한다
# 궁수가 공격하는 적은 거리가 D 이하 중 가장 가깝고
# 거리가 같은 적들이면 제일 왼쪽놈을 공격한다
# 같은 놈이 여러번 공격당할 수 있음
# 공격 끝나면 적이 이동

# 궁수가 죽일 수 있는 적의 최대수를 구핼

import itertools


# n, m, d (궁수의 공격거리)
n, m, d = map(int, input().split())
target = [list(map(int, input().split())) for _ in range(m)]

shoot = [i for i in range(m)]
com_shoot = list(itertools.combinations(shoot, 3))

for i in target:
    print(i)

for i in com_shoot:
    a, b, c = i[0], i[1], i[2]
    attack = [0 for _ in range(m)]
    attack[a] = 7
    attack[b] = 7
    attack[c] = 7

    target.append(attack)


