# Baekjoon
# https://www.acmicpc.net/problem/17136

# N x N 색종이가 5 종류가 있고 각각 5개씩 있다
# 맵에 1과 0으로 적혀 있는데, 1을 모두 가려야한다
# 0에는 색종이가 있으면 안되고
# 1을 모두 없애는데 실패하면 -1 출력
# 1을 모두 가리는데 필요한 색종이의 최소 갯수를 구해라

def f(n, s): # n : 사용한 종이수, s : 남은 1
    global minV
    if s==0:
        if minV>n:
            minV = n
    elif minV == 4:
        return
    elif sum(paper)==0:
        return
    else:
        for i in range(10):
            for j in range(10):
                if m[i][j]==1 and visited[i][j] ==0: # 왼쪽 모서리로 가정
                    for k in range(5, 0, -1): # 덮는 크기

                        if paper[k]>0 and i+k<=10 and j+k<=10: # 종이가 남아있고
                            cover = 0
                            for r in range(i, i+k):
                                for c in range(j, j+k):
                                    if visited[r][c]==0:
                                        cover += m[r][c]
                            if cover==(k*k): # 덮어지면
                                for r in range(i, i + k):
                                    for c in range(j, j + k):
                                        visited[r][c] = 1
                                paper[k] -= 1
                                f(n+1, s-k*k)
                                for r in range(i, i + k):
                                    for c in range(j, j + k):
                                        visited[r][c] = 0
                                paper[k] += 1
                    return

m = [list(map(int, input().split()))for _ in range(10)]
visited = [[0]*10 for _ in range(10)]
minV = 26
s = 0
paper = [0, 5, 5, 5, 5, 5]
for i in range(10):
    for j in range(10):
        if m[i][j]==1:
            s += 1
f(0, s)
if minV == 26:
    minV = -1
print(minV)

'''

0 0 0 0 0 0 0 0 0 0
0 1 1 0 0 0 0 0 0 0
0 1 1 1 0 0 0 0 0 0
0 0 1 1 1 1 1 0 0 0
0 0 0 1 1 1 1 0 0 0
0 0 0 0 1 1 1 0 0 0
0 0 1 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0

0 0 0 0 0 0 0 0 0 0
0 1 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 1 0 0 0 0 0
0 0 0 0 0 1 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 1 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0

'''