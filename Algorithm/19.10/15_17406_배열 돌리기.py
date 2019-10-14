# Baekjoon
# https://www.acmicpc.net/problem/17406

# 배열이 주어진다
# 각 행의 합 중에서 가장 작은 값을 뽑는데,,
# 회전 연산에 따라 배열을 회전 시키고나서
# 각 행의 합 중에서 최소값을 출력한다

n, m, k = map(int, input().split())
# n : 가로수
# m : 세로수

mapp = [list(map(int, input().split())) for _ in range(n)]
func = [list(map(int, input().split())) for _ in range(k)]

for i in range(k):
    start = [func[i][0] - func[i][2],func[i][1] - func[i][2]]
    end = [func[i][0] + func[i][2],func[i][1] + func[i][2]]
    garos = end[0] - start[0] + 1
    print(start[0])
    print(end[0])
    print()


'''

5 6 2
1 2 3 2 5 6
3 8 7 2 1 3
8 2 3 1 4 5
3 4 5 1 1 1
9 3 2 1 4 3
3 4 2
4 2 1

'''