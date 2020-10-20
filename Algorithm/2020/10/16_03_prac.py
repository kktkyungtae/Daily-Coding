


# for i in range(x - 1, n, x):
#     if d == 0:
#         wonpan[i] = wonpan[i][-k:] + wonpan[i][:-k]
#         vst[i] = vst[i][-k:] + vst[i][:-k]
#     else:
#         wonpan[i] = wonpan[i][k:] + wonpan[i][:k]
#         vst[i] = vst[i][k:] + vst[i][:k]

a = [[i for i in range(1,6)]] * 5

print(a[0][-2:])
print(a[0][:-2])
a[0] = a[0][-2:] + a[0][:-2]
print(a)
a[1] = a[1][ 2:] + a[1][: 2]
print(a)