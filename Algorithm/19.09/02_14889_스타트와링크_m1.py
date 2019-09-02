from itertools import combinations

isize = int(input())

info = []
for _ in range(isize):
    info.append(list(map(int, input().split())))

# print(info)

player = [i for i in range(isize)]
combi_player = list(combinations(player, int(isize//2)))

result = []
for i in range(int(len(combi_player)/2)):
    start = combi_player[i]
    link = player[:]

    start_result = 0
    link_result = 0

    # start
    for s_1 in start:
        link.remove(s_1)
        for s_2 in start:
            start_result += info[s_1][s_2]

    # link
    for l_1 in link:
        for l_2 in link:
            link_result += info[l_1][l_2]

    result.append(abs(start_result - link_result))

print(min(result))


