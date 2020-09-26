# 3라인에 걸쳐서 윷결과가 주어진다
# 그 결과를 출력해라
# 0 1 0 1
# 1 1 1 0
# 0 0 1 1

# 1 3개 A
# 1 2개 B
# 1 1개 C
# 1 4개 E
# 1 0개 D


yut_li = []
for i in range(3):
    yut_li.append(list(map(int, input().split())))

one_li = []
for j in range(3):
    one_li.append(yut_li[j].count(1))

for k in one_li:
    if k == 0:
        print('D')
    elif k == 1:
        print('C')
    elif k == 2:
        print('B')
    elif k == 3:
        print('A')
    else:
        print('E')

