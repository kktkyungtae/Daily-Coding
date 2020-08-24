# Programmers
# https://programmers.co.kr/learn/courses/30/lessons/42748?language=python3

# 주어진 조건대로 배열을 자르고, 해당하는 순서의 값을 출력하라

array = [1, 5, 2, 6, 3, 7, 4]
commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]


def solution(array, commands):
    answer = []
    for i in range(len(commands)):
        temp = array[commands[i][0] -1 :commands[i][1]]
        temp.sort()
        answer.append(temp[commands[i][2] - 1])

    return answer

print(solution(array, commands))