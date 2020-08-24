
import sys
sys.stdin = open("5_민석이의과제체크.txt", "r")

def my_sort(a):
    for i in range(len(a)-1):
        for j in range(len(a)-i-1):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
    return a

T = int(input())
for t in range(1, T+1):
    total, save = map(int, input().split())
    nums = list(map(int, input().split()))

    result = []
    for i in range(1,total+1):
        if i not in nums:
            result.append(i)
    result = my_sort(result)
    print(f"#{t}", end=" ")
    for i in result:
        print(i, end=" ")
    print()





