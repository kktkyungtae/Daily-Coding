import sys
sys.stdin = open('전기버스.txt', 'r')

T = int(input())

def success(char_station):
    for i in range(len(char_station)):
        if char_station[i+1] - char_station[i] > K:
            return False
        else:
            return True



for test_case in range(T):
    K,N,M = map(int,input().split())
    o_station = [0 for _ in range(N+1)]
    char_station = list(map(int,input().split()))
    for i in char_station:
        o_station[i] += 1
    # [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0]

    start = 0
    cnt = 0

    if success(char_station) == False:
        print('#{} 0'.format(test_case+1))
    else:
        while True:
            for x in range(K,0,-1):
                if start + x > N:
                    start = N
                    break
                elif o_station[start+x] == 1:
                    start = start + x
                    cnt += 1
                    break
            if start == N:

                break


        print('#{} {}'.format(test_case+1,cnt))