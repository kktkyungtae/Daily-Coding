# 윤년이면 1, 아니면 0 출력
# 4의 배수고 100의 배수가 아니면 윤년
# 400의 배수면 윤년

A = int(input())

if A % 4 == 0 and A % 100 != 0:
    print(1)
elif A % 400 == 0 and A%100 ==0:
    print(1)
else:
    print(0)
