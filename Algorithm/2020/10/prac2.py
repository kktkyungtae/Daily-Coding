from collections import deque

q = deque((x for x in range(10)))

print(q)
q.pop()
print(q)
