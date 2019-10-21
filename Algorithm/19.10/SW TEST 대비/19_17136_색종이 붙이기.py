# Baekjoon
# https://www.acmicpc.net/problem/17136

# N x N 색종이가 5 종류가 있고 각각 5개씩 있다
# 맵에 1과 0으로 적혀 있는데, 1을 모두 가려야한다
# 0에는 색종이가 있으면 안되고
# 1을 모두 없애는데 실패하면 -1 출력
# 1을 모두 가리는데 필요한 색종이의 최소 갯수를 구해라


def func(n, ones): # 사용한 종이수 , 1의 갯수
    global minV

    # 1의 갯수가 0일 때
    if ones == 0:
        if minV > n:
            minV = n
    ### minV 4는 뭐지...??
    elif minV == 4:
        return
    # 종이 다 쓰면 끝
    elif sum(paper) == 0:
        return
    else:
        for i in range(10):
            for j in range(10):
                if Map[i][j] == 1 and visited[i][j] == False: # 만나는 1의 왼쪽 모서리 부터 시작
                    for k in range(5, 0, -1): # 종이 크기대로 대보기
                        cover = 0
                        if paper[k] > 0 and i + k <= 10 and j + k <= 10: # 종이가 남아있고, 범위 안일 때
                            for x in range(i, i + k):
                                for y in range(j, j + k):
                                    if visited[x][y] == False and Map[x][y] == 1:
                                        cover += 1
                            if cover == (k*k): # 종이 크기만큼 연결된 1이 덮어지면
                                for x in range(i, i + k):
                                    for y in range(j, j + k):
                                        visited[x][y] = True
                                paper[k] -= 1
                                func(n+1, ones - k*k)

                                ### 여기서 왜 다시 visited False..?
                                for x in range(i, i+k):
                                    for y in range(j, j + k):
                                        visited[x][y] = False
                                paper[k] += 1

                    return


Map = [list(map(int, input().split())) for _ in range(10)]
visited = [[False] * 10 for _ in range(10)]
minV = 26
ones = 0

paper = [0, 5, 5, 5, 5, 5]

for i in range(10):
    for j in range(10):
        if Map[i][j] == 1:
            ones += 1

func(0, ones) # 사용한 종이수 , 1의 갯수

if minV == 26:
    print(-1)
else:
    print(minV)