def perm(n):
    global li_perm
    global result, temp

    if n == 0:
        if result < (temp * 100):
            result = (temp * 100)
        return

    for i in range(N):
        if not i in li_perm:
            li_perm.append(i)
            if li_P[li_perm[-1]][len(li_perm) - 1] > 1:
                temp *= (li_P[li_perm[-1]][len(li_perm) - 1] * 0.01)
                if temp >= (result * 0.01):
                    perm(n - 1)
                temp /= (li_P[li_perm[-1]][len(li_perm) - 1] * 0.01)
            li_perm.remove(i)


T = int(input())

for t in range(T):
    N = int(input())
    li_P = []
    for n in range(N):
        li_P.append(list(map(float, input().split())))

    li_perm = []
    result = 0
    temp = 1
    perm(len(li_P))

    print("#{}".format(t + 1), end=" ")
    print("%0.6f" % result)