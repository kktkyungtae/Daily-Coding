N = int(input())
n = 0
cnt = 0
tf = False

if N > 1022:
    print(-1)

else:
    while (N != cnt):
        if len(str(n)) == 1:
            cnt += 1
            n += 1
        else:
            for i in range(len(str(n))-1):
                if int(str(n)[i]) <= int(str(n)[i+1]):
                    n += (10**(len(str(n))-i-1))-(10**(len(str(n))-i-2)*int(str(n)[i+1]))
                    for j in range(len(str(n))-1):
                        if int(str(n)[j]) <= int(str(n)[j+1]):
                            break
                    else:
                        cnt += 1
                    break
            else:
                n += 1
                if str(n)[-1] != str(n)[-2]:
                    cnt += 1

    print(n)