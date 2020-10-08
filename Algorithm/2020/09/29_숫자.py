# 주어진 두 정수 사이의 숫자를 모두 출력하라

a, b = map(int, input().split())

# a < b
if a < b:
    print(b-a-1)
    for i in range(a+1, b):
        print(i, end=' ')

# a > b
elif a > b:
    print(a-b-1)
    for i in range(b+1, a):
        print(i, end=' ')
# a == b
else:
    print(0)
