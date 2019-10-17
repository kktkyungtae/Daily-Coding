# Baekjoon
# https://www.acmicpc.net/problem/17135

# 2차 배열의 적들이 몰려오는데
# 3명의 궁수를 배치해서 적을 죽여야한다
# 2차 배열에 마지막행에 한 칸을 추가해서 궁수를 배치하고
# 최대로 죽일 수 있는 적의 수를 출력해라

# 거리가 가까운적 부터 죽이고, 거리가 같으면 왼쪽 부터

from itertools import combinations

def deepcopy(arr):
    return [i[:] for i in arr][:]

def attack(combi, board, N, M, D):
    cnt = 0

    for i in range(N, 0, -1):   # 성벽의 위치
        recover = []
        for j in combi:         # 궁수의 위치
            flag = False
            for d in range(1, D+1):
                for s in range(-(d-1), (d-1)+1):
                    f = d - abs(s)

                    r = i - f
                    c = j + s

                    if 0 <= r < N and 0 <= c < M and board[r][c] != 0:
                        if board[r][c] == 1:
                            cnt += 1
                            board[r][c] = 2
                            recover.append([r, c])
                        flag = True
                        break
                if flag:
                    break
        for r, c in recover:
            board[r][c] = 0
    return cnt

N, M, D = list(map(int, input().split()))
board = list(list(map(int, input().split())) for _ in range(N))
archer_combi = combinations([i for i in range(M)], 3)

max_output = 0
for combi in archer_combi:
    cur_max = attack(combi, deepcopy(board), N, M, D)
    max_output = max(max_output, cur_max)

print(max_output)


'''

5 5 1
0 0 0 0 0
0 0 0 0 0
0 0 0 0 0
0 0 0 0 0
1 1 1 1 1

'''