
import sys
sys.stdin = open("색칠하기", "r")

T = int(input())
for tc in range(1, T+1):

    basic = [[0] * 10 for _ in range(10)]
    a = int(input())
    arr1 = []  # 배열 받기
    for i in range(a):
        b = list(map(int, input().split()))
        arr1.append(b)

    cnt = 0   # 겹치는 공간을 셀 변수
    for c in range(a):  # 2차원 배열의 행의 수 만큼 실행
        # i의 범위 : 해당 행의 0번지와 2번지
        # j의 범위 : 해당 행의 1번지와 3번지
        for i in range(arr1[c][0], arr1[c][2]+1) :
            for j in range(arr1[c][1], arr1[c][3]+1):
                # 만약, 해당 행,열의 도화지가 0이거나, 자신의 색깔이면 그냥 색칠
                if basic[i][j] == 0 or basic[i][j] == arr1[c][4]:
                    basic[i][j] = arr1[c][4]
                # 아니면, 겹쳤다는 뜻의 3을 추가하고 cnt+=1
                else:
                    basic[i][j] = 3
                    cnt += 1
    print("#{} {}".format(tc, cnt))


