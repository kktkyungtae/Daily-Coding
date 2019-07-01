import sys
sys.stdin = open('input/03_input.txt','r')

t = int(input())
for tc in range(t):
    n = int(input())

    hurdle = list(map(int,input().split()))

    top = [0]
    down = [0]

    for i in range(len(hurdle)-1):
        if hurdle[i] - hurdle[i+1] < 0:
            top.append(abs(hurdle[i] - hurdle[i+1]))
        elif hurdle[i] - hurdle[i+1] > 0:
            down.append(abs(hurdle[i] - hurdle[i + 1]))
        elif hurdle[i] - hurdle[i+1] == 0:
            top.append(0)
            down.append(0)

    print("#{} {} {}".format(tc+1, max(top), max(down)))