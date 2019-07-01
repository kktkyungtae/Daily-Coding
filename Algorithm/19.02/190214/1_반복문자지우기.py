import sys
sys.stdin = open("반복문자지우기.txt","r")

T = int(input())

for t in range(T):
    msg = input()

    stack = ['PADDING']
    for letter in msg:
        if stack[-1] == letter:
            stack.pop()
        else:
            stack.append(letter)
    
    print(f"#{t+1} {len(stack)-1}")