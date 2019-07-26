# Baekjoon

# 주어지는 단어들의 조합으로 서로 같아질 수 있는지 판별
# 같으면 Possible
# 틀리면 impossible

tc = int(input())

for _ in range(tc):
    a, b = input().split()
    if sorted(a) == sorted(b):
        print('Possible')
    else:
        print('Impossible')
    print(a)
