# Programmers
# https://programmers.co.kr/learn/courses/30/lessons/43163?language=python3

# 주어진 시작 단어가 타겟 단어가 되도록
# 따로 주어진 워드 리스트를 참조해서
# 시작 단어에서 한 단어씩 변경해서 타켓 단어가 될 수 있는
# 변환 과정의 수를 출력하라

def solution(begin, target, words):
    answer = [begin]

    if target not in words:
        return 0

    ans_cnt = 0

    while len(words) != 0:
        for i in answer:
            temp = []
            for word in words:
                cnt = 0
                for j in range(len(i)):
                    if i[j] == word[j]:
                        cnt += 1
                    if cnt == 2:
                        break

                if cnt == 1:
                    temp.append(word)
                    words.remove(word)
        ans_cnt += 1

        if target in temp:
            return ans_cnt
        else:
            answer = temp

    return 0