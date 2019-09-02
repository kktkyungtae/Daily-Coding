import itertools

isize = int(input())

info = []
for i in range(isize) :
    info.append(list(map(int, input().split())))

# 플레이어 리스트
player_list = [i for i in range(isize)]
# 팀 조합 만들기
combination_player = list(itertools.combinations(player_list, int(isize/2)))

# print(combination_player)
#
result = []
# 어짜피 첫 조합이랑 제일 뒷 조합이랑 같은 팀이니까
for i in range((int(len(combination_player)/2))):
    # 조합의 첫팀 스타트팀부터
    start = list(combination_player[i])
    # 링크팀을 복사해준다
    link = player_list[:]

    start_result = 0
    link_result = 0

    for first_start in start:
        link.remove(first_start)
        for second_start in start:
            start_result += info[first_start][second_start]

    for first_link in link:
        for second_link in link:
            link_result += info[first_link][second_link]

    result.append(abs(start_result-link_result))
    # print(start)
    # print(link)

print(min(result))