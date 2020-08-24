import sys
sys.stdin = open('2578_input.txt','r')

def bingo_check(mc):
    for i in range(5):
        for j in range(5):
            if bingo[i][j] == mc:
                check[i][j] = True
                return None

def finish_check():
    cnt = 0
    # 가로 검색
    for i in range(5):
        if not False in check[i]:
            cnt += 1

    # 세로 검색
    for j in range(5):
        temp = True
        for i in range(5):
            if check[i][j] == False:
                temp = False
                break
        if temp== True:
            cnt += 1

    # 대각선 아래 검색
    temp = True
    for i in range(5):
        if check[i][i] == False:
            temp = False
            break
    if temp == True:
        cnt += 1

    # 대각선 위 검색
    temp = True
    for i in range(5):
        if check[i][4 - i] == False:
            temp = False
            break
    if temp == True:
        cnt += 1

    if cnt >= 3:
        return True
    else:
        return False


bingo = []
check = [[False] * 5 for _ in range(5)]

for _ in range(5):
    bingo.append(list(map(int, input().split())))

mc = []

for _ in range(5):
    mc.extend(list(map(int, input().split())))

for m in range(len(mc)):
    bingo_check(mc[m])
    if m > 10 and finish_check():
        print(m + 1)
        break