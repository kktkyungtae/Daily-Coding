def solution(N):
    answer = [0, 0]

    for i in range(2, 10):
        trans = [1]
        num = N
        while num > 1:
            trans.append(num % i)
            num //= i

        exits = 1

        for k in range(len(trans)):
            if trans[k] != 0:
                exits *= trans[k]

        if answer[1] <= exits:
            answer[1] = exits
            answer[0] = i

    return answer

print(solution(10))

