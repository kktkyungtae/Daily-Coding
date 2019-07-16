# Baekjoon
# 1 부터 20까지 주어진 숫자를
# 주어지는 10개의 구간에서 순서를 역으로 바꿔서 출력해라


# 숫자 리스트
num_li = [x for x in range(1, 21)]

# 인풋 받기
lens = []
for t in range(10):
    le = list(map(int, input().split()))
    lens.append(le)

# 인덱스 조심!
for i in range(10):
    num_li[lens[i][0]-1:lens[i][1]] = reversed(num_li[lens[i][0]-1:lens[i][1]])

for k in num_li:
    print(k, end=' ')