import sys
sys.stdin = open('13_input.txt','r')

for tc in range(10):

    n = int(input())

    mag_li = []
    for i in range(100):
        mag_li.append(list(map(int,input().split())))

    cnt = 0
    for g in range(100):
        magnet = []
        for s in range(100):
            if mag_li[s][g] != 0:
                magnet.append(mag_li[s][g])

        for i in range(len(magnet)-1):
            if magnet[i] == 1 and magnet[i+1] == 2:
                cnt += 1

    print("#{} {}".format(tc+1,cnt))