def simulation(y, x, weight):
    global n, answer
    queue = [(y, x, weight, weight)]

    while queue:
        curr_y, curr_x, curr_w, cnt = queue.pop(0)

        # BFS 로 상어의 현재위치에서 각 먹이감 까지 거리를 계산한 배열을 가져온다.
        dist_arr = bfs(curr_y, curr_x, curr_w)
        dist = 987654321
        for i in range(n):
            for j in range(n):
                if 0 < MAP[i][j] < curr_w and MAP[i][j] != 9:
                    tmp = dist_arr[i][j]  # BFS로 계산한 해당 좌표의 최소값을 임시로 할당

                    # 중요. tmp = -1 일 경우 tmp 최소값으로 -1이 잡혀서 틀림
                    if tmp < dist and tmp != -1:
                        next_y, next_x = i, j
                        dist = tmp

        if dist != 987654321:
            # 상어의 위치를 바꾼다.
            MAP[curr_y][curr_x] = 0
            MAP[next_y][next_x] = 9
            answer += dist  # 거리를 더해줌
            cnt -= 1  # 무게 수만큼 물고기를 먹을 때 체중 증가해야하므로

            if cnt == 0:  # 0이 되는 순간
                curr_w += 1  # 현재 체중을 1 증가
                cnt = curr_w  # 무게 수는 다시 현재 체중으로 초기화

            # # 상어 이동경로 출력
            # print("############")
            # for m in MAP:
            #     print(m)
            # print("dist {} cumul {} weight {}".format(dist, answer, curr_w))
            # print()

            queue.append((next_y, next_x, curr_w, cnt))  # 상어의 위치와 무게를 queue에 넣어서 시뮬레이션을 반복한다.


def bfs(st_y, st_x, weight):  # 상어의 현재위치에서 각 먹이감 까지 거리를 계산
    global n
    q = [(st_y, st_x)]
    check = [[-1] * n for _ in range(n)]
    check[st_y][st_x] = 0
    while q:
        c_y, c_x = q.pop(0)
        for d in direction:
            n_y = c_y + d[0]
            n_x = c_x + d[1]
            if 0 <= n_y < n and 0 <= n_x < n:
                if MAP[n_y][n_x] <= weight and check[n_y][n_x] == -1:
                    check[n_y][n_x] = check[c_y][c_x] + 1
                    q.append((n_y, n_x))
    return check


direction = ((-1, 0), (1, 0), (0, -1), (0, 1))
n = int(input())
MAP = [list(map(int, input().split())) for _ in range(n)]
answer = 0

flag = True
for i in range(n):
    for j in range(n):
        if MAP[i][j] == 9:
            simulation(i, j, 2)
            flag = False
            break
    if not flag:
        break

print(answer)

'''
#input
3
9 2 2
2 2 3
1 3 1

#output
2


#input
2
9 3
3 1

#output
0
'''