import sys
sys.stdin = open("이진탐색", "r")

def find(P, A):
    l = 1  # 첫페이지
    r = P  # 마지막페이지
    c = int((1 + P) / 2)  # 페이지 반으로 줄임
    cnt = 1
    while (c != A):
        cnt += 1
        mid = int((l + r) / 2)
        if (mid == A):
            return cnt
            break
        elif (mid > A):
            r = mid
        else:
            l = mid
    return cnt


T = int(input())
for t in range(1,T+1):

    P,A,B = map(int,input().split())
    a = find(P, A)
    b = find(P, B)

    if(a==b):
        print(f"#{t} 0")
    elif(b<a):
        print(f"#{t} B")
    else:
        print(f"#{t} A")



