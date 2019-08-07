# Baekjoon
# 완전탐색

# N,N 에 사탕의 색깔이 주어지고
# 인접한 두 칸을 고르고, 두 칸의 사탕의 순서를 바꾼다
# 이 때, 같은 색으로 연결된 가장 긴 행이나 열의 갯수를 출력해라

# 연속 행 세기
def inline(row):
    temp = 1
    result = 1
    for i in range(len(row)-1):
        if row[i] == row[i+1]:
            temp += 1
        else:
            result = max(result, temp)
            temp = 1
    return max(result, temp)


# 바꾸기
def swap(i1, j1, i2, j2):
    mat[i1][j1], mat[i2][j2] = mat[i2][j2], mat[i1][j1]
    swap_1 = max(inline(row) for row in mat)
    swap_2 = max(inline(row) for row in zip(*mat))
    mat[i1][j1], mat[i2][j2] = mat[i2][j2], mat[i1][j1]

    return max(swap_1, swap_2)

tc = int(input())

mat = []
for t in range(tc):
    mat.append(list(input()))

result = 0

# 가로 바꾸기
for i in range(tc):
    for j in range(tc-1):
        result = max(result, swap(i, j, i, j+1))

# 세로 바꾸기
for i in range(tc-1):
    for j in range(tc):
        result = max(result, swap(i, j, i+1, j))


print(result)