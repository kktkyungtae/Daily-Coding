mapp = [[i, i] for i in range(1,10)]
mapp2 = [[i, i] for i in range(1,10)]
print(mapp)
for i in range(8, 1, -1):
    mapp[i][0] = mapp[i-1][0]
print(mapp)

print(mapp2)
for i in range(1, 8):
    mapp2[i+1][0] = mapp2[i][0]


print(mapp2)