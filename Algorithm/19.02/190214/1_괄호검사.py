import sys
sys.stdin = open("괄호검사.txt","r")

T = int(input())

for t in range(T):
    msg = input()
    bracket_li = [['(',')'], ['{','}']]
    bracket = ''

    for m in msg:
        for bl in bracket_li:
            for brk in bl:
                if m == brk:
                    bracket += m

    stack = []
    result = '0'
    error_tf = False
    
    for b in bracket:
        if b == bracket_li[0][0] or b == bracket_li[1][0]:
            stack.append(b)
        else:
            if stack:
                if stack[-1]==bracket_li[0][0] and b==bracket_li[0][1]:
                    stack.pop()
                elif stack[-1]==bracket_li[1][0] and b==bracket_li[1][1]:
                    stack.pop()
                else:
                    error_tf = True
                    break
            else:
                error_tf = True
                break

    if not error_tf:
        if not stack:
            result = '1'

    print(f"#{t+1} {result}")