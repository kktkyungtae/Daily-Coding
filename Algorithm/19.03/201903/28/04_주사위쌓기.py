import sys
sys.stdin = open('04_input.txt','r')

N = int(input())
jusawi = [list(map(int,input().split())) for _ in range(N)]

def back_num(a):
    if a == 0:
        return 5
    elif a == 1:
        return 3
    elif a == 2:
        return 4
    elif a == 3:
        return 1
    elif a == 4:
        return 2
    else:
        return 0

result = []
for i in range(6):
    # 첫 밑면 선택하기 + 윗면 고르기
    buttom = jusawi[0][i]
    mid_up = jusawi[0][back_num(i)]

    k = 1
    temp = []
    temp_max = 0
    for j in jusawi[0]:
        if j != buttom and j != mid_up:
            if temp_max < j:
                temp_max = j
    temp.append(temp_max)
    while k < N:
        temp_max = 0
        buttom = mid_up
        mid_up = jusawi[k][back_num(jusawi[k].index(buttom))]
        for h in jusawi[k]:
            if h != buttom and h != mid_up:
                if temp_max < h:
                    temp_max = h
        temp.append(temp_max)
        k+=1

    result.append(sum(temp))
print(max(result))