# 9명의 난쟁이들 중에 키의 합이 100이 되는 7명을 찾아서
# 랜덤으로 출력해라
import copy

shorts = []
temp_short = []
for _ in range(9):
    shorts.append(int(input()))

flag = False
for i in range(9):
    for j in range(9):
        if i == j:
            continue
        else:
            if shorts[i] + shorts[j] == sum(shorts) - 100:
                keep = [i, j]
                flag = True
                break
    if flag == True:
        break

shorts.remove(shorts[keep[0]])
shorts.remove(shorts[keep[1]-1])

shorts.sort()
for i in range(7):
    print(shorts[i])


