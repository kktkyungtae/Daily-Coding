import sys
sys.stdin = open('05_input.txt','r')

T = int(input())
money = [50000, 10000, 5000, 1000, 500, 100, 50, 10]


for tc in range(T):
    W = int(input())
    money_cnt = [0] * len(money)

    if W % 10 == 0:
        for i in range(len(money)):
            if money[i] <= W:
                temp = W//money[i]
                W = W - temp * money[i]
                money_cnt[i] = temp
                temp = 0
            elif W == 0:
                break
    else:
        pass
    print("#{}".format(tc+1))
    for i in money_cnt:
        print(i, end=' ')
    print()


    #
    # i = 0
    # while True:
    #     if W - money[i] >= 0:
    #         temp = W // money[i]
    #         W = W - money[i] * temp
    #         i += 1
    #         money_cnt[i] += temp
    #     elif W == 0:
    #         break
    # print(money_cnt)





