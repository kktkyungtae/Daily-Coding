#2304

import sys
sys.stdin = open('01_input.txt','r')

N = int(input())
store = []
# [[2, 4], [4, 6], [5, 3], [8, 10], [11, 4], [13, 6], [15, 8]]

for i in range(N):
    temp_store = list(map(int,input().split()))
    store.append(temp_store)
    store.sort()

h_list = []
# [4, 6, 3, 10, 4, 6, 8]
for i in range(len(store)):
    h_list.append(store[i][1])

real_store = [0] * (store[N-1][0] + 1)
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# [0, 0, 4, 0, 6, 3, 0, 0, 10, 0, 0, 4, 0, 6, 0, 8]

for i in range(len(store)):
    real_store[store[i][0]] = store[i][1]

max_h = 0
for i in range(store[0][0],store[N-1][0] + 1):
    if real_store[i] > max_h:
        max_h = real_store[i]
max_idx = real_store.index(max_h)

# 최대값을 중심으로 좌에서 > 최대값까지
temp_h = 0
for j in range(store[0][0], max_idx):
    if j+1 <= max_idx:
        if real_store[j] > real_store[j+1]:
            temp_h = real_store[j]
            real_store[j + 1] = temp_h
        else:
            temp_h = real_store[j + 1]
            real_store[j + 1] = temp_h

# 최대값을 중심으로 우에서 > 최대값까지
temp_h = 0
for r in range(store[N-1][0],max_idx, -1):
    if real_store[r] > real_store[r-1]:
        temp_h = real_store[i]
        real_store[r - 1] = temp_h
    else:
        temp_h = real_store[r - 1]

print(sum(real_store))