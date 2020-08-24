# Baekjoon
# 한 세트에는 0번부터 9번까지 숫자가 하나씩 들어있다. 다솜이의 방 번호가 주어졌을 때,
# 필요한 세트의 개수의 최솟값을 출력하시오. (6은 9를 뒤집어서 이용할 수 있고, 9는 6을 뒤집어서 이용할 수 있다.)


num = list(map(int,input()))

sett = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

for j in range(len(num)):
    if num[j] == 9:
        num[j] = 6
    else:
        pass

for i in num:
    sett[i] += 1

sett[6] = sett[6] // 2 + sett[6] % 2

print(max(sett))