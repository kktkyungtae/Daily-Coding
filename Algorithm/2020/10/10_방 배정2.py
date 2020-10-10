# Baekjoon
# 수학여행 방배정

# 입력
# 학생수   방정원
# 성별(여 : 0, 남 : 1)   학년

# 학생들을 모두 배정하기 위한 최소한의 방의 수를 구하라.

n, k = map(int, input().split())
rooms = [[0,0] for _ in range(6)]
students = []

for t in range(n):
    noms = list(map(int,input().split()))
    students.append(noms)

for i in range(n):
    if students[i][0] == 1:
        rooms[students[i][1]-1][0] += 1
    else:
        rooms[students[i][1]-1][1] += 1

reserve = 0
for h in range(6):
    for l in range(2):
        if rooms[h][l] % k == 0:
            reserve += rooms[h][l] // k
        else:
            reserve += (rooms[h][l] // k) + 1
print(rooms)
print(reserve)