N = int(input())
switch = list(map(int,input().split()))
switch.insert(0,N)
gen = int(input())
gen_list = []

for g in range(gen):
    gen_list.append(list(map(int,input().split())))

for g in range(gen):
    if gen_list[g][0] == 1:
        k = gen_list[g][1]
        for i in range(k,len(switch),k):
            if switch[i] == 1:
                switch[i] = 0
            else:
                switch[i] = 1


    else:
        temp = 1
        k = gen_list[g][1]
        while True:
            if k - temp >=1 and k + temp <= N:
                if switch[k - temp] == switch[k + temp]:
                    if switch[k - temp] == 1:
                        switch[k - temp] = 0
                        switch[k + temp] = 0
                    else:
                        switch[k - temp] = 1
                        switch[k + temp] = 1
                    temp += 1
                else:
                    break
            else:
                break

        if switch[k] == 1:
            switch[k] = 0
        else:
            switch[k] = 1

for x in range(1, len(switch)):
    print(switch[x], end=' ')
    if x % 20 == 0 and x != 0:
        print()