# https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AWhVVhNaS8EDFAW_&contestProbId=AV7GLXqKAWYDFAXB&probBoxId=AWlQi_tavioDFAVS&type=PROBLEM&problemBoxTitle=17%EC%9D%BC%EC%B0%A8%283%EC%9B%946%EC%9D%BC%29&problemBoxCnt=4

N = int(input())
map_list = [list(map(int, list(input()))) for _ in range(N)]
answer = 0
half = N//2
back = half
for i in range(N):
    for j in range(abs(N // 2 - i), abs(N - N//2)):
        map_list[i][j] = 0
    if i < half:
        back = back - 1
    else:
        back += 1
for i in map_list:
    print(i)


# print('#{} {}'.format(t, answer)

# 5
# 14054
# 44250
# 02032
# 51204
# 52212