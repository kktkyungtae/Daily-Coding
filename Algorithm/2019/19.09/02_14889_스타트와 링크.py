# baekjoon
# https://www.acmicpc.net/problem/14889

# 스타트와 링크로 팀을 나눠라
# 그때, 각 플레이어들은 같은 팀이 되었을 때
# 할당 되는 점수가 다르다
# 두 팀간의 차이가 가장 작게 나누고
# 그 차이를 출력해라

from itertools import combinations

n = int(input())
field = [list(map(int, input().split())) for _ in range(n)]

# print(field)

player = [i for i in range(n)]

# 리스트라고 선언해야 된다. 걍 대괄호로 묶으니까 이상하네..
combi_player = list(combinations(player, int(n//2)))

# print(combi_player)

result = []
for i in range(int(len(combi_player)//2)):
    start = combi_player[i]
    link = player[:]

    start_result = 0
    link_result = 0

    for k in start:
        link.remove(k)
        for l in start:
            start_result += field[k][l]

    for k in link:
        for l in link:
            link_result += field[k][l]

    result.append(abs(start_result - link_result))

print(min(result))
