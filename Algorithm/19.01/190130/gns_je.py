import sys
sys.stdin = open("GNS_test_input.txt", "r")


T = int(input())
for t in range(1, T+1):
    a = int(input().split()[1])
    b = input().split()
    b_dict = {'ZRO': 0, 'ONE': 1, 'TWO': 2, 'THR': 3,
               'FOR': 4, 'FIV': 5, 'SIX': 6, 'SVN': 7, 'EGT': 8, 'NIN': 9}
    result = [[], [], [], [], [], [], [], [], [], []]

    for i in range(len(b)):
        result[b_dict[b[i]]].append(b[i])

    print(f'#{t}')
    for i in range(10):
        for j in range(len(result[i])):
            print(result[i][j], end=" ")
    print()