# Programmers
# https://programmers.co.kr/learn/courses/30/lessons/42842?language=python3

# 갈색과 빨간색이 주어지는데
# 빨간색을 중앙에 두고 갈색이 둘러싼다
# 최종 사각형의 가로 세로 길이를 구하라

def solution(brown, red):
    for a in range(1, int(red**(0.5)) +1):
        if red % a == 0:
            b = red // a

            if 2*a + 2*b + 4 == brown:
                return [b+2, a+2]