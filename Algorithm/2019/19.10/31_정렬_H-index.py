# Programmers
# https://programmers.co.kr/learn/courses/30/lessons/42747?language=python3

def solution(c):
    for i, x in enumerate(sorted(c)):
        if x >= len(c) - i:
            return len(c) - i

    return 0


c = [3, 0, 6, 1, 5]
print(solution(c))
print(sorted(c))