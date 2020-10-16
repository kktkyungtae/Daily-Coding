import sys

from collections import deque

input = sys.stdin.readline
# N = 원판의 개수
# M = 원판에 적힌 숫자의 개수
N, M, T = map(int, input().split())
board = [list(map(int, input().strip().split())) for _ in range(N)]
# x, d, k : x의 배수인 원판을 d 방향으로 k칸 회전
spiner = [list(map(int, input().strip().split())) for _ in range(T)]


# i 번째 원 k 칸 회전
def spintLeft(i, k):
    board[i] = board[i][k:] + board[i][:k]


# i 번째 원 k 칸 회전
def spinRight(i, k):
    board[i] = board[i][-k:] + board[i][:-k]


def spin(x, d, k):
    if (d == 0):
        for i in range(1, N + 1):
            if i % x == 0:
                # print("spin", i, "th circle to Right", k, "times")
                spinRight(i - 1, k)
    else:
        for i in range(1, N + 1):
            if i % x == 0:
                # print("spin", i, "th circle to Left", k, "times")
                spintLeft(i - 1, k)


def removeNum():
    set = []
    visit = [[False] * M for _ in range (N)]
    ## change deque into list
    for i in range(N):
        for j in range(M):
            if not visit[i][j]:
                for k in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
                    ro = i + k[0]
                    co = j + k[1]
                    if co == M:
                        co = 0
                    # if  0<=ro and ro <N and 0<=co and co< M :
                    if ro >= 0 and ro < N :
                        if board[i][j] != 0 and board[ro][co] == board[i][j]:
                            set.append([i, j])
                            visit[i][j] = True
                            set.append([ro, co])
                            visit[i][j] = True
    if len(set) == 0:
        ifNoSameNum();
    else:
        for a, b in set:
            board[a][b] = 0
    ## change list ot deque


def ifNoSameNum():
    average = 0
    count = 0
    for i in range(N):
        for j in range(M):
            if board[i][j] != 0:
                average += board[i][j]
                count += 1
    if count == 0 :
        return
    average = average / count
    for i in range(N):
        for j in range(M):
            if board[i][j] != 0:
                if board[i][j] > average:
                    board[i][j] -= 1
                elif board[i][j] < average:
                    board[i][j] += 1


def getAnser():
    ans = 0
    for i in range(N):
        for j in range(M):
            ans += board[i][j]
    return ans


def solve():
    for i in range(T):
        spin(spiner[i][0], spiner[i][1], spiner[i][2])
        removeNum()
    print(getAnser())


solve()
