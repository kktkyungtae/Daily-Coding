# baekjoon
# https://www.acmicpc.net/problem/2583

# 주어진 영역에 사각형들을 덮을 건데,
# 덮고 나서 안덮힌 구역의 수 및 각각의 넓이를 구하라

m, n, k = map(int, input().split())
nemos = [list(map(int, input().split())) for _ in range(k)]
mapp = [[-1]*(n+1) for _ in range(m+1)]



