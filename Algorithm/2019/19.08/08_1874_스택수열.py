# Baekjoon


t = int(input())
num_li = [int(input()) for _ in range(t)]
stack = []
num = 1
result = []
for i in num_li:
    while i >= num:
        stack.append(num)
        result.append('+')
        num += 1
    if stack[-1] == i:
        result.append('-')
        stack.pop(-1)
    else:
        print('NO')
        break
else:
    for i in result:
        print(i)