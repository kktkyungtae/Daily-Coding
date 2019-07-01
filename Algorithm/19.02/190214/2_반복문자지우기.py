import sys

sys.stdin = open("반복문자지우기.txt", "r")

def delete(s):
    for i in range(len(s)-1):
        if s[i] == s[i+1]:
            s = s[:i] + s[i+1+1:]
            delete(s)
            break
    result.append(s)

T = int(input())
for test_case in range(1, T + 1):
    S = input()
    result = []
    delete(S)
    
    print(f'#{test_case} {len(result[0])}')