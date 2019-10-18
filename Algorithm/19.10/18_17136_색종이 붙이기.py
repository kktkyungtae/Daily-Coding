# Baekjoon
# https://www.acmicpc.net/problem/17136

# N x N 색종이가 5 종류가 있고 각각 5개씩 있다
# 맵에 1과 0으로 적혀 있는데, 1을 모두 가려야한다
# 0에는 색종이가 있으면 안되고
# 1을 모두 없애는데 실패하면 -1 출력
# 1을 모두 가리는데 필요한 색종이의 최소 갯수를 구해라

Map = [list(map(int, input().split())) for _ in range(10)]

