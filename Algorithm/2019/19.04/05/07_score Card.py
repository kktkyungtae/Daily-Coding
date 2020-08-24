import sys
sys.stdin=open('input/07_input.txt','r')

t = int(input())
for t in range(t):
    n, k = map(int,input().split())
    score_li = list(map(int,input().split()))
    score_li.sort()
    score_li.reverse()

    result = []
    for i in range(k):
        result.append(score_li[i])

    print("#{} {}".format(t+1, sum(result)))

