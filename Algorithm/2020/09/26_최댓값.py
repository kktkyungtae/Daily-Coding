# 주어진 숫자들 중에 최댓값을 출력하고
# 몇 번째 수 인지도 출력 하시오

num_li = []
for i in range(9):
    k = int(input())
    num_li.append(k)

print(max(num_li))
print(num_li.index(max(num_li)) + 1)