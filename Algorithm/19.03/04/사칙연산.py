def postorder(T):
    global postfix
    if T:
        postorder(tree[T][1])
        postorder(tree[T][2])
        postfix.append(tree[T][0])


for t in range(10):
    N = int(input())

    # [data, left, right]
    tree = [[0] * 3 for _ in range(N + 1)]

    for n in range(N):
        input_ = input().split()

        if len(input_) == 2:
            tree[int(input_[0])][0] = int(input_[1])

        else:
            tree[int(input_[0])][0] = input_[1]
            tree[int(input_[0])][1] = int(input_[2])
            tree[int(input_[0])][2] = int(input_[3])

    postfix = []
    postorder(1)

    stack = []

    for pf in postfix:
        if pf == '+':
            b = stack.pop()
            a = stack.pop()
            temp = a + b
            stack.append(temp)
        elif pf == '-':
            b = stack.pop()
            a = stack.pop()
            temp = a - b
            stack.append(temp)
        elif pf == '*':
            b = stack.pop()
            a = stack.pop()
            temp = a * b
            stack.append(temp)
        elif pf == '/':
            b = stack.pop()
            a = stack.pop()
            temp = a // b
            stack.append(temp)
        else:
            stack.append(pf)

    print("#{} {}".format(t + 1, stack.pop()))