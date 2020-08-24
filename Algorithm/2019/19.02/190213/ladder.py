import sys
sys.stdin= open("ladder.txt","r")

for test_case in range(1, 11):
    input()
    ladder = []
    test = []
    dy = [1, -1, 0]


    for i in range(100):
        ladder.append(list(map(int, input().split())))

    for i, v in enumerate(ladder[0]):
        if v == 1:
            test.append(i)
    print(ladder)
    for i in test:
        result = i
        for j in range(100):
            if i + dy[0] <= 99 and ladder[j][i + dy[0]] == 1:
                while (i + dy[0] <= 99 and ladder[j + 1][i + dy[0]] == 0):
                    i += 1
                i += 1
            elif i + dy[1] >= 0 and ladder[j][i + dy[1]] == 1:
                while (i + dy[1] >= 0 and ladder[j + 1][i + dy[1]] == 0):
                    i -= 1
                i -= 1
        if ladder[j][i] == 2:
            break

    # print(f'#{test_case} {result}')