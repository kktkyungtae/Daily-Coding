# Baekjoon
# 중요도를 고려해서 원하는 문서가 몇번째 출력되는지 구하라

t = int(input())
for i in range(t):
    n, w = map(int, input())
    v = int(input())

    li = [l for l in range(1, n+1)]
    if len(li) == 0:
        print(li[0])
    else:


