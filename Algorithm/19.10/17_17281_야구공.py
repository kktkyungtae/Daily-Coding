# Baekjoon
# https://www.acmicpc.net/problem/17281

# 야구룰
# 1번 선수가 4번 타자일 때,
# 주어진 조건에 맞도록
# 나머지 선수들의 타순을 모두 결정해라

import itertools

# def 결과에 따라 값을 더해주고 루에 진루 시켜주는 함수
def start(real_hit):
    i = 0
    ans = 0
    for hits in hitttt:
        out = 0
        base1, base2, base3 = 0, 0, 0

        while out < 3:
            if hits[real_hit[i]] == 0:
                out += 1

            elif hits[real_hit[i]] == 1:
                ans += base3
                base1, base2, base3 = 1, base1, base2

            elif hits[real_hit[i]] == 2:
                ans += base3 + base2
                base1, base2, base3 = 0, 1, base1

            elif hits[real_hit[i]] == 3:
                ans += base3 + base2 + base1
                base1, base2, base3 = 0, 0, 1

            elif hits[real_hit[i]] == 4:
                ans += base3 + base2 + base1 + 1
                base1, base2, base3 = 0, 0, 0

            i = (i+1) % 9

    return ans

# input
inning = int(input())
hitttt = [list(map(int, input().split())) for _ in range(inning)]

ans = 0
for hit in itertools.permutations(range(1, 9), 8):
    real_hit = list(hit[:3]) + [0] + list(hit[3:])
    ans = max(start(real_hit), ans)

print(ans)
'''
2
4 0 0 0 0 0 0 0 0
4 0 0 0 0 0 0 0 0

2
0 4 4 4 4 4 4 4 4
0 4 4 4 4 4 4 4 4
'''