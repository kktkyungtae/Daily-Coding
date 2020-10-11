from collections import deque

q = deque()
q_2 = deque()
q_3 = deque()

q.append((1,2))
q_3.append([1,2])

l = deque()
l.append((7,9))
m, l = l.pop()
print(m)

print(q)
print(q[0])
print(q[0][0])
print(q.popleft())

q.append((3,4))
x, y = q.popleft()
print(x)

print()

print(q_3)
print(q_3[0])
print(q_3[0][0])
print(q_3.popleft())

q_3.append([3,4])
d, f = q_3.popleft()
print(d)