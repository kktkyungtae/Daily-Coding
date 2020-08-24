import itertools

li = [2,4,7,10]

new_li = list(itertools.combinations(li, 2))

print(new_li)

# 조합을 만들어 주는 콤비네이션!

# 쓰려면

new_li2 = list(itertools.combinations(li,3))


print(new_li2)
