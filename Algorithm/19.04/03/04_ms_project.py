import sys
sys.stdin = open('04_input.txt','r')

T = int(input())
for tc in range(T):
    N, K = map(int,input().split())

    num_list = list(map(int,input().split()))
    num_list.sort()

    student = []
    for i in range(1,N+1):
        student.append(i)

    for j in range(len(num_list)):
        if num_list[j] in student:
            student.remove(num_list[j])

    print("#{}".format(tc + 1), end=" ")
    for k in student:
        print(k, end=' ')
    print()


