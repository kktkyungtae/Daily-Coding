# 숫자 세 개가 주어진다. 이 숫자는 1보다 크거나 같고, 1,000,000보다 작거나 같다.
# 이 숫자는 모두 다르다.
#
# 제일 작은 수, 그 다음 수, 제일 큰 수를 차례대로 출력한다.

lists = list(map(int,input().split()))

lists.sort()

for i in lists:
    print(i, end=' ')