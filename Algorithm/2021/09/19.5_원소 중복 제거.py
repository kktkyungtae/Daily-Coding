
# 1차 배열 중복 제거
alpa = [1, 1, 1, 2, 2, 2, 3, 3, 3]
alpa = list(set(alpa))

print(alpa)

# 2차 배열 중복 제거
lists = [[1, 2], [1, 2], [1], [1]]
lists_m = list(set(map(tuple, lists)))

print(lists_m)
