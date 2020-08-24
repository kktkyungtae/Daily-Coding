import sys
sys.stdin = open('12_input.txt','r')

for _ in range(10):
    tc = int(input())
    ladder = []
    for k in range(100):
        temp = list(map(int,input().split()))
        ladder.append(temp)

    start = 0
    for s in range(100):
        if ladder[99][s] == 2:
            start = s
            break

    for i in range(98,-1,-1):
        # 왼쪽 경계 일때
        if start == 0:
            if ladder[i][start + 1] == 1:
                start += 1
                while ladder[i][start + 1] == 1:
                    start += 1
                    if start == 99:
                        break


        # 오른쪽 경계 일때
        elif start == 99:
            if ladder[i][start - 1] == 1:
                start -= 1
                while ladder[i][start - 1] == 1:
                    start -= 1
                    if start == 0:
                        break


        # 경계가 아닐 때
        else:
            if ladder[i][start - 1] == 1:
                start -= 1
                while ladder[i][start - 1] == 1:
                    start -= 1
                    if start == 0:
                        break

            elif ladder[i][start + 1] == 1:
                start += 1
                while ladder[i][start + 1] == 1:
                    start += 1
                    if start == 99:
                        break

    print("#{} {}".format(tc,start))