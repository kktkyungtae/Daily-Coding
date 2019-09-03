#baekjoon
# https://www.acmicpc.net/problem/14889

# 스타트와 링크라는 두팀으로 팀을 나누는데
# 각 인원들마다 한 팀으로 묶였을 때, 할당되는 점수가 있다
# 그 점수들의 차이가 가장 작도록 팀을 짜고
# 그 차이를 출력해라

from itertools import combinations

isize = int(input())

info = []
for _ in range(isize):
    info.append(list(map(int, input().split())))

# print(info)

player = [i for i in range(isize)]
combi_player = list(combinations(player, int(isize//2)))

# print(player)
# print(combi_player)

result = []

# 절반만 보면됨
# > 플레이어 조합에 처음이랑 끝이랑 같이 묶이니까
for i in range(int(len(combi_player)/2)):

    # 첫 스타트 팀
    start = combi_player[i]
    # 첫 링크 팀 : 플레이어 전체 리스트 복사
    link = player[:]

    # 각 팀으로 나누었을 때 중간 결과
    start_result = 0
    link_result = 0

    # start
    for s_1 in start:
        # 스타트에서 선택된 플레이어를 링크에서 뺌
        link.remove(s_1)
        for s_2 in start:
            start_result += info[s_1][s_2]

    # link
    for l_1 in link:
        for l_2 in link:
            link_result += info[l_1][l_2]

    result.append(abs(start_result - link_result))

print(min(result))


