from collections import deque

q = deque((x for x in range(10)))
print('기본', q)

q.rotate()
print('rotate()', q)


q.rotate(-2)
print('rotate(-2)', q)

q.rotate(2)
print('rotate(2)', q)