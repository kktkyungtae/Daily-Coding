import sys
sys.stdin = open("특별한정렬", "r")

# 들어온 배열을 정렬하고 시작할거임
def my_sort(a):
    for i in range(len(a)-1):
        for j in range(len(a)-i-1):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]

T = int(input())
for t in range(1,T+1):
    m = int(input())
    a = list(map(int, input().split()))

    my_sort(a)

    b = [0]*m   # 빈 배열 공간 만들어 놓고

    max1 = m-1  # 최대값의 index : 정렬된 a배열의 길이 - 1
    min1 = 0    # 최소값의 index : 절렬된 a배열의 0

    # 이제 a배열의 길이만큼 돌건데,
    for i in range(m):
        if(i==0 or i%2==0):    # 만약 b의 index가 0이거나, 짝수면 -> 최대값이 거꾸로 들어가야함
            b[i] = str(a[max1])  # b배열에 a배열의 최대값 인덱스를 넣음
            max1 -= 1            # 다음 b의 index부터는 다음 최대값을 넣어야함
        else:                   # b의 index가 홀수 ?  최소값이 순서대로 들어가야함
            b[i] = str(a[min1])
            min1+=1

    print(f'#{t}', end=" ")
    for i in range(10):
        print(b[i], end=" ")
    print()




