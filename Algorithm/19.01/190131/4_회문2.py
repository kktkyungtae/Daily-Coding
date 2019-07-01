
import sys
sys.stdin = open("4_회문2.txt","r")
1
def longest_palindrom(s):
    # 비교할 문자열의 길이를 지정 : 문자열의 제일 긴 길이부터 0까지 -1씩 줄여나감
    for i in range(len(s), 0, -1):
        # 짧아진 길이 만큼 앞뒤로 이동시키며 비교 : 줄인 길이 만큼 문자열의 시작점을 이동시키며 비교해야 한다.
        # 때문에 +1을 해준다.
        for j in range(len(s) - i + 1):
            # j는 부분 문자열의 시작 index, i는 부분 문자열의 길이
            if(s[j:j+i] == my_reverse(s[j:j+i])):
                return i
def my_max(arr):
    max1 = 0
    for i in range(len(arr)):
        if arr[i] > max1:
            max1=arr[i]
    return max1

def my_reverse(s):
    result = ""
    for i in range(len(s)-1, -1, -1):
        result += s[i]
    return result

for tc in range(10):
    tc = input()
    result = []
    answer = []
    for num in range(100):
        result += [input()]

    # 가로 회문찾기
    for i in range(100):
        a = longest_palindrom(result[i])
        answer.append(a)

    # 세로 회문 찾기
    c = []
    for i in range(100):
        b = ''
        for j in range(100):
            b += result[j][i]
        c.append(b)
    for i in range(100):
        a = longest_palindrom(c[i])
        answer.append(a)

    print(f"#{tc} {my_max(answer)}")




