# Baekjoon
# 주어진 사각형을 잘라서
# 0은 가로 1은 세로
# 가장 큰 넓이를 구하라

garo, sero = map(int, input().split())
tc = int(input())

# 가로, 세로 칸 만들기 위한 리스트
garo_cut = [0]
sero_cut = [0]

# 잘라야되는 가로, 세로 만들기
for _ in range(tc):
    temp = input().split()
    if temp[0] == '0':
        sero_cut.append(int(temp[1]))
    else:
        garo_cut.append(int(temp[1]))

max_garo = 0
max_sero = 0

# 잘자야되는 수를 오름차 순으로
garo_cut.sort()
sero_cut.sort()

# 가로, 세로 마지막 길이 추가
garo_cut.append(garo)
sero_cut.append(sero)

# MAX 가로 길이의 차이 구하기
for i in range(len(garo_cut)-1):
    if max_garo < garo_cut[i+1] - garo_cut[i]:
        max_garo = garo_cut[i+1] - garo_cut[i]

# MAX 세로 길이의 차이 구하기
for i in range(len(sero_cut)-1):
    if max_sero < sero_cut[i+1] - sero_cut[i]:
        max_sero = sero_cut[i+1] - sero_cut[i]

# MAX 넓이 구하기
print(max_garo*max_sero)