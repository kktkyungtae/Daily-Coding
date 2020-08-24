import sys
sys.stdin = open('01_input.txt','r')

def perm(cnt, total):
    global result
    if total <= result:  # 소수는 곱할수록 작아지므로 저장되어있던 result와 비교해서 작으면 pass
        return

    if cnt == N:  # 끝까지 왔을 때
        if total > result:  # 비교해서 리턴
            result = total
        return

    for i in range(N):
        if visited[i] == 1:  # 이미 방문했으면 다음 i로
            pass

        visited[i] = 1
        perm(cnt + 1, total * work_per[cnt][i])
        visited[i] = 0

T = int(input())

for tc in range(T):
    N = int(input())
    work_per = []
    for n in range(N):
        work_per.append(list(map(int,input().split())))

    for i in range(N):
        for j in range(N):
            work_per[i][j] /= 100

    visited = [0] * N
    result = 0

    perm(0, 1)
    print("#%s %0.6f" % (tc + 1, result * 100))
