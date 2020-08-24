# 네 개의 윷짝을 던져서 배(0)와 등(1)
# A도(0 : 1 개, 1 : 3 개), B개(0 : 2 개, 1 ; 2 개), C걸(0 : 3 개, 1 : 1 개), D윷(0 : 4 개), 모(1 : 4 개)

yut_list = []
result = []

for j in range(3):
    yut = list(map(int, input().split()))
    yut_list.append(yut)


for i in range(3):
    k = 0
    for q in range(4):
        k = k + yut_list[i][q]
    result.append(k)

for a in result:
    if a == 4:
        print('E')
    elif a == 3:
        print('A')
    elif a == 2:
        print('B')
    elif a == 1:
        print('C')
    else:
        print('D')