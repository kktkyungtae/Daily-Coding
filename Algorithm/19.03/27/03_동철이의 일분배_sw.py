import sys
sys.stdin=open('03_input.txt','r')

def bt(work, prob):
    global max
    if prob <= max: return
    if work == n:
        if prob > max:
            max = prob
        return
    for i in range(n):
        if done[i] == 0:
            done[i] = 1
            bt(work + 1, prob * board[i][work])
            done[i] = 0


for tc in range(int(input())):
    n = int(input())
    board = [list(map(int, input().split())) for _ in range(n)]
    for i in range(n):
        for j in range(n):
            board[i][j] = board[i][j] / 100
    done = [0] * n
    max = 0
    bt(0, 1)
    print("#%d %0.6f" % (tc + 1, max * 100))