# 숫자의 갯수
# 주어지는 숫자들 중에서
# 찾으려는 숫자가 몇개인지 출력해라

n = int(input())
n_li = list(map(int, input().split()))
k = int(input())

print(n_li.count(k))