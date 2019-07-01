def check(li_A):
    global min_value

    sum_A = 0
    sum_B = 0

    li_B = [x for x in range(N)]
    for a in li_A:
        li_B.remove(a)

    for i in range(len(li_A)):
        for j in range(i + 1, len(li_A)):
            sum_A += li[li_A[i]][li_A[j]]
            sum_A += li[li_A[j]][li_A[i]]
            sum_B += li[li_B[i]][li_B[j]]
            sum_B += li[li_B[j]][li_B[i]]

    if min_value > abs(sum_A - sum_B):
        min_value = abs(sum_A - sum_B)


def find(start, n):
    global li_A
    if n == 0:
        check(li_A)
        return

    for i in range(start, N):
        li_A.append(i)
        find(i + 1, n - 1)
        li_A.remove(i)


N = int(input())

li = []
li_A = []

min_value = 9999

for n in range(N):
    li.append(list(map(int, input().split())))

find(0, N // 2)

print(min_value)