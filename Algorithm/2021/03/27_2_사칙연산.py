# 두개의 숫자를 입력 받고
# 원하는 연산을 출력해주는 것

a, b, c = map(int, input().split())

if c == 1:
    print(a+b)
elif c == 2:
    print(a-b)
elif c == 3:
    print(a//b)
elif c == 4:
    print(a*b)
else:
    print('바보야')

