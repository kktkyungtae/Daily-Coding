# 입력 받을 때! 벌써 까먹었네
# 일단 받은 입력을 List로 받는게 처리하기 편해
# 편한 정도가 아니라 List로 받아야 되는게 더 많다
# 띄어쓰기로 input이 되어 있으면, split!

lists = list(map(int,input().split()))

lists.sort()

for i in lists:
    print(i, end=' ')