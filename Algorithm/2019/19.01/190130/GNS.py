import sys
sys.stdin = open("GNS_test_input.txt", "r")

T = int(input())

for tc in range(1, T+1):
    a = int(input().split()[1])
    b = input().split()

    print(f'#{tc}')