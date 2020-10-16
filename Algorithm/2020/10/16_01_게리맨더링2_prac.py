mapp = [[1] * 7 for _ in range(7)]
for k in mapp:
    print(k)
cnt1, cnt2, cnt3, cnt4, d = 0, 0, 0, 0, 0
lx = 3
x = 1
y = 3


# 첫번째 선거구
# x 범위는 왼쪽 x좌표, y 범위는 기준좌표의 y값
for i in range(lx):
    for j in range(y + 1):
        # 인덱스가 기준점과 같아지면
        # 끝!
        # 그리고 d + 1 해주는건, 울타리 따라서 내려가야 하니까
        if [i, j] == [x + d, y - d]:
            d += 1
            break
        print(i, j)
        cnt1 += mapp[i][j]
        mapp[i][j] = 0

print()
for i in mapp:
    print(i)