# 오름차순 정렬
# 백준 11650
# 2차원 평면 위의 점 N개가 주어진다.
# 좌표를 x좌표가 증가하는 순으로, x좌표가 같으면 y좌표가 증가하는 순서로 정렬한 다음 출력하는 프로그램을 작성하시오.

n = int(input())

arr = []
for i in range(n):
    arr.append(list(map(int, input().split())))

arr.sort(key=lambda x:(x[0], x[1]))


for a in arr:
    print(str(a[0]) + " " + str(a[1]))

# Input
# 5
# 3 4
# 1 1
# 1 -1
# 2 2
# 3 3

# Output
# 1 -1
# 1 1
# 2 2
# 3 3
# 3 4