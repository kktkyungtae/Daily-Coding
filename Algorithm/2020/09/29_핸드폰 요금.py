# Y : 30초 마다 10원
# M : 60초 마다 15월
# 20보다 큰 자연수의 통화시간이 주어진다. 더 싼 요금제와 금액을 써라

call = int(input())
c_times = list(map(int, input().split()))

Y_sum = []
M_sum = []

for i in range(call):
    if c_times[i] % 30 == 0:
        Y_sum.append(10 * (c_times[i] // 30))
    else:
        Y_sum.append(10*(c_times[i] // 30) + 10)

for i in range(call):
    if c_times[i] % 60 == 0:
        M_sum.append(15 * (c_times[i] // 60))
    else:
        M_sum.append(15*(c_times[i] // 60) + 15)

if sum(Y_sum) < sum(M_sum):
    print('Y', sum(Y_sum))
elif sum(Y_sum) > sum(M_sum):
    print('M', sum(M_sum))
else:
    print('Y M', sum(Y_sum))