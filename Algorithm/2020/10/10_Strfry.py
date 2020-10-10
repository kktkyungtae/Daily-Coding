# 주어진 수의 쌍의 문자열이
# strfry로 무작위로 섞었을때 가능한지 아닌지 출력해라

tc = int(input())
w_li = []
for i in range(tc):
    w_li.append(list(map(str, input().split())))

# for k in range(tc):
#     w_li[k][0] = str(w_li[k][0])
#     w_li[k][1] = str(w_li[k][1])

for j in range(tc):
    if sorted(w_li[j][0]) == sorted(w_li[j][1]):
        print('Possible')
    else:
        print('Impossible')
