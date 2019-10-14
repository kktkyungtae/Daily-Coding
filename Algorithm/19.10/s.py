import itertools

k = 3

for i in itertools.permutations(range(k),3):
    print(i)
print()

for i in itertools.combinations(range(k),3):
    print(i)

