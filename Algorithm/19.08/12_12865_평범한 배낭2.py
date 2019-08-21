def knapsack1(n, k):
    array = [[0 for _ in range(k+1)] for _ in range(n+1)]
    for i in range(1, n+1):
        for s in range(1, k+1):
            if w_list[i-1] > s: # 물건의 무게가 s보다 크면
                array[i][s] = array[i - 1][s]
            else: # 물건의 무게가 s보다 작거나 같으면
                array[i][s] = max(v_list[i-1] + array[i-1][s-w_list[i-1]], array[i-1][s])
            print('%2d' % array[i][s], end=' ')
        print()
    return array[n][k]

N, K = map(int, input().split())
w_list = []
v_list = []
for _ in range(N):
    w, v = map(int, input().split())
    w_list.append(w)
    v_list.append(v)

print(knapsack1(N, K))