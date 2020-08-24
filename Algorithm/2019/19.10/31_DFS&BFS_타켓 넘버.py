# Programmers
# https://programmers.co.kr/learn/courses/30/lessons/43165?language=python3

def solution(numbers, target):
    answer_li = [0]

    for i in numbers:
        temp_li = []

        for j in answer_li:
            temp_li.append(j + i)
            temp_li.append(j - i)

        answer_li = temp_li
    answer = answer_li.count(target)

    return answer

a = [1,1,1,1,1]
b = 3
print(solution(a, b))