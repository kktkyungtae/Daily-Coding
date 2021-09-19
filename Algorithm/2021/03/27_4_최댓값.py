num_li = []
for i in range(9):
    num_li.append(int(input()))

k = max(num_li)

print(k)
print(num_li.index(k) + 1)

