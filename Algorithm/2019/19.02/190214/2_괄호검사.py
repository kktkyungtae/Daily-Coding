import sys
sys.stdin = open("괄호검사.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    str_ = input()
    stack = [0]*len(str_)
    tmp = -1

    for s in str_:
        if s == '{':
            tmp += 1
            stack[tmp] = s
        elif s == '(':
            tmp += 1
            stack[tmp] = s
        elif s == '}':
            if stack[tmp] == '{':
                stack.pop(tmp)
                tmp -= 1
            else:
                tmp = 0
                break
        elif s == ')':
            if stack[tmp] == '(':
                stack.pop(tmp)
                tmp -= 1
            else:
                tmp = 0
                break
    else:
        if stack[0] != 0:
           tmp = 0
        else:
            tmp = 1 
    
    print(f'#{test_case} {tmp}')