n = int(input())
for _ in range(n):
    a, *arr = map(int, input().split())
    print(a, arr)
# 3
# 4 10 20 30 40
# 3 7 5 12
# 3 125 15 25

## 한줄에, 수의 갯수 n과 그 뒤에 n개의 정수가 주어질 때
# n 뒤의 정수들을 바로 배열로 만들고 싶을 때