mp, vrs = map(int, input().split())
mapp = []
for i in range(mp):
    mapp.append(list(map(int, input().split())))

vrs_xy = []
for i in range(mp):
    for j in range(mp):
        if mapp[i][j] == 2:
            vrs_xy.append([i,j])

print(mapp)
print(vrs_xy)