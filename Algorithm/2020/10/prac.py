n_li = []
for i in range(3):
    n_li.append(int(input()))

n_lili = str(n_li[0] * n_li[1] * n_li[2])
print(n_lili)
count = []
for j in range(10):
    count.append(n_lili.count(str(j)))

for k in count:
    print(k)

