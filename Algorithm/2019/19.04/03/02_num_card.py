import sys
sys.stdin = open('02_input.txt','r')

t = int(input())
for tc in range(t):
    n = int(input())

    num_li = list(map(int,input()))
    card_count = [0 for _ in range(10)]

    for i in range(len(num_li)):
        temp = num_li.count(i)
        card_count[i] = temp

    print(card_count)





# T = int(input())
# for test_case in range(1, T + 1):
#
#     a = int(input())
#     n = list(map(int, input()))
#     cnt = 0
#     num = 0
#     for i in range(10):
#         if n.count(i) >= cnt:
#             cnt = n.count(i)
#             num = i
#     print(n)
#     print("#{} {} {}".format(test_case,num,cnt))