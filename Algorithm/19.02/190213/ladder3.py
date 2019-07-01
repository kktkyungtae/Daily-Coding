import sys
sys.stdin= open("ladder.txt","r")

for tc in range(10):

    # input
    tnum = input()
    ladder = []
    for _ in range(100):
        ladder.append(input().split())

    for i in range(100):
        if ladder[-1][i] == '2':
            location = i

    for _ in range(100 - 1, -1, -1):
        if location >= 1 and ladder[_][location - 1] == '1':  # 왼쪽
            location -= 1
            for j in range(location - 1, -1, -1):
                if ladder[_][j] == '0':
                    break
                location -= 1

        elif location <= 98 and ladder[_][location + 1] == '1':  # 오른쪽
            location += 1
            for j in range(location + 1, 100):
                if ladder[_][j] == '0':
                    break
                location += 1

    print("#{} {}".format(tc + 1, location))