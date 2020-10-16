# https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AWhVVhNaS8EDFAW_&contestProbId=AV7GLXqKAWYDFAXB&probBoxId=AWlQi_tavioDFAVS&type=PROBLEM&problemBoxTitle=17%EC%9D%BC%EC%B0%A8%283%EC%9B%946%EC%9D%BC%29&problemBoxCnt=4

T = int(input())
for t in range(1, T+1):
    N = int(input())
    map_list = [list(map(int, list(input()))) for _ in range(N)]
    t_N = N//2
    change = -1
    answer = 0
    for i in range(N):
        if i >= N//2:
            change = 1
        for j in range(abs(i-N//2), abs(N-t_N)):
            answer += map_list[i][j]
        t_N += change

    print('#{} {}'.format(t, answer))