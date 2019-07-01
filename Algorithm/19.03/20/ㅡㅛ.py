T = int(input())
temp_code = ['0001101', '0011001', '0010011', '0111101', '0100011', '0110001', '0101111', '0111011', '0110111', '0001011']


for tc in range(T):
    N, M = map(int, input().split())
    temp_li = []
    for n in range(N):
        temp_li.append(list(input()))

    key = []
    for i in temp_li:
