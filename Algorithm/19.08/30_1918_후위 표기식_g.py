op_order = {"-": 1, "+": 1, "*": 2, "/": 2, "(": 0}

ex = input()
stack = []

# 식 돌기
for c in ex:
    # 식중에 파라미터가 있으면,
    if c in op_order.keys():
        # 스택이 비었거나, (면 스택에 넣기
        if not stack or c == '(':
            stack.append(c)
        # 아니면,
        else:
            while stack and op_order[c] <= op_order[stack[-1]]:
                print(stack.pop(), end='')
            stack.append(c)

    elif c == ')':
        while stack and stack[-1] != '(':
            print(stack.pop(), end='')

        if stack and stack[-1] == '(':
            stack.pop()

    else:
        print(c, end='')

while stack:
    print(stack.pop(), end='')