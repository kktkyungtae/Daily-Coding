# Crackerjack

from collections import deque

# 연한 구역으로 인해 블록을 삭제해서,
# 블록 이동을 탐색하는 함수
# go()에는 생성된 블록만 움직이고, MoveBlock()에는 바닥부분을 제외한 모든 칸을 탐색
def MoveBlock():
    global green, blue
    for i in range(1, 6):
        for j in range(4):
            # Green
            if green[5-i][j] > 0:
                # 블록이 있으면, 이 블록이 1*1 블록인지 아닌지 체크
                block_state = FindMulti_Block_state(5-i, j, green[5-i][j], True)
                # 블록을 움직여주는 move()함수에 정보를 담아 보내
                move(block_state, green[5-i][j], True)
            # Blue
            if blue[j][5 - i] > 0:
                block_state = FindMulti_Block_state(j, 5 - i, blue[j][5 - i], False)
                move(block_state, blue[j][5 - i], False)

# 블록이 2,3번이라면, 그 인접 블록의 좌표도 찾아주는 함수
def FindMulti_Block_state(i, j, value, isGreen):
    global blue, green
    result = deque()
    result.append([i, j])
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]

    for l in range(4):
        nx = i + dx[i]
        ny = j + dy[i]

        if isGreen == True and 0 <= nx < 6 and 0 <= ny < 4 and green[nx][ny] == value:
            result.append([nx, ny])
            break
        if isGreen == False and 0 <= ny < 6 and 0 <= nx < 4 and blue[nx][ny] == value:
            result.append([nx, ny])
            break

    return result

# 삭제 후 블록을 이동시켜주는 함수. 1,2,3 블록 모두 이동
def move(block_state, value, isGreen):
    global green, blue
    now_x, now_y = block_state[0]
    near_x, near_y = -1, -1

    if len(block_state) == 2:
        near_x, near_y = block_state[1]
    if isGreen == True:
        while True:
            next_x = now_x + 1
            if near_x != -1:
                next_near_x = near_x + 1
            if next_x >= 6 or green[near_x][now_y] > 0:
                break
            if near_x != -1 and green[next_near_x][near_y] > 0 and green[next_near_x][near_y] != value:
                break
            green[next_x][now_y] = value
            green[now_x][now_y] = 0
            now_x = next_x
            if near_x != -1:
                green[next_near_x][near_y] = value
                green[near_x][near_y] = 0
                near_x = next_near_x

    else:
        while True:
            next_y = now_y + 1
            if near_y != -1:
                next_near_y = neary + 1
            if next_y >= 6 or blue[now_x][next_y] > 0:
                break
            if neary != -1 and blue[near_x][next_near_y] > 0 and blue[near_x][next_near_y] != value:
                break
            blue[now_x][next_y] = value;
            blue[now_x][now_y] = 0;
            nowy = next_y
            if neary != -1: blue[near_x][next_near_y] = value
            blue[near_x][neary] = 0
            neary = next_near_y


# 연한 구역에 블록이 있을 경우, 그 수 만큼 바닥 부분부터 지우는 함수
def FindDelete():
    global green, blue
    count_g, count_b = 0, 0

    # Green 첫번째 줄 탐색
    # 해당 line에 하나라도 블록이 있으면 나머지는 탐색하지 않아도 돼
    for i in range(4):
        if green[0][i] != 0:
            count_g += 1
            break
    # Green 두번째 줄 탐색
    for i in range(4):
        if green[1][i] != 0:
            count_g += 1
            break

    # Blue 탐색
    for i in range(4):
        if blue[i][0] != 0:
            count_b += 1
            break
    for i in range(4):
        if blue[i][1] != 0:
            count_b += 1
            break

    # 연한 구역에 있던 줄 만큼, 밑 줄을 삭제
    for i in range(count_g):
        for j in range(4):
            green[5-i][j] = 0
    ########
    for i in range(count_b):
        for j in range(4):
            blue[j][5-i] = 0

    # 연한 구역에 블록이 있었는지 없었는지 반환
    if count_g ==0 and count_b==0:
        return False
    else:
        return True


def CheckClear():
    global green, blue, ans
    result_g = []
    result_b = []

    # Green
    for i in range(4):
        count = 0
        for j in range(4):
            # 칸이 0인 경우, count변수에 -1, 0이 아니면 (블록이 있으면_ +1을 저장
            # 종료조건을 위해 블록의 가장 바닥부터 탐색
            if green[5-i][j] == 0:
                break
            else:
                count += 1
        # 해당 row가 차있으면 그 row의 index 저장
        if count == 4:
            result_g.append(5-i)

    # blue
    for i in range(4):
        count = 0
        for j in range(4):
            if blue[j][5-i] == 0:
                break
            else:
                count += 1
        if count == 4:
            result_b.append(5-i)

    # 저장된 줄 index가 존재할 경우, 해당 줄을 모두 0으로 바꿔주고 점수를 +1
    if len(result_g) > 0:
        for gx in result_g:
            ans += 1
            for j in range(4):
                green[gx][j] = 0
    if len(result_b) > 0:
        for by in result_b:
            ans += 1
            for j in range(4):
                blue[j][by] = 0

    # 줄이 사라졌는지 안사라졌는지 체크하기 위해 결과를 반환
    if len(result_g) > 0 or len(result_b) > 0:
        return True
    else:
        return False


def go(block, index):
    global ans
    t, x, y = block
    # 좌표값과 블록 모형을 Green, Blue에 각각 생성
    if t == 1:
        green[0][y] = index
        blue[x][0] = index
    elif t == 2:
        green[0][y] = index
        green[0][y+1] = index
        blue[x][0] = index
        blue[x+1][0] = index
    else:
        green[0][y] = index
        green[1][y] = index
        blue[x][0] = index
        blue[x+1][0] = index

    now_x, now_y = 0, 0

    # 생성한 블록을 벽이나, 다른 블록에 부딪힐 때까지 move
    if t == 1:
        # Move Green
        while True:
            next_x = now_x + 1
            # 범위를 벗어나거나, 다른 블록이 있을 때까지 반복
            if next_x > 5 or green[next_x][y] != 0:
                break
            # 블록 이동
            green[next_x][y] = green[now_x][y]
            green[now_x][y] = 0
            now_x = next_x
        # Move blue
        while True:
            next_y = now_y + 1
            if next_y > 5 or blue[x][next_y] != 0:
                break
            blue[x][next_y] = blue[x][now_y]
            blue[x][now_y] = 0
            now_y = next_y

    elif t == 3:
        # Move Green
        now_x = 1
        while True:
            next_x = now_x + 1
            if next_x > 5 or green[next_x][y] != 0:
                break
            # t = 3 은 2칸 차지하니까,, next_x가 기준이고, x 한칸 위 까지 한 블럭으로 처리
            green[next_x][y] = green[now_x][y]
            green[now_x-1][y] = 0

            # 한칸씩 내려가면서 탐색해야하니깐
            now_x = next_x

        # Move Blue
        while True:
            next_y = now_y + 2
            if blue[x][next_y] != 0 or next_y > 5:
                break
            blue[x][next_y] = blue[x][now_y]
            blue[x+1][next_y] = blue[x+1][now_y]
            blue[x][now_y], blue[x+1][now_y] = 0, 0
            now_y = next_y

    else:
        # Move green
        while True:
            next_x = now_x + 1
            if next_x > 5 or green[next_x][y] != 0:
                break
            green[next_x][y] = green[now_x][y]
            green[next_x][y+1] = green[now_x][y+1]
            green[now_x][y+1], green[now_x][y] = 0, 0
            now_x = next_x

        # Move Blue
        now_y = 1
        while True:
            next_y = now_y + 1
            if next_y > 5 or blue[x][next_y] != 0:
                break
            blue[x][next_y] = blue[x][now_y]
            now_y = now_x


    # 채워진 블럭을 없애거나, 연한 구역에 블럭이 있으면 행렬을 삭제하고 점수 +1
    # 점수계산 및 행렬삭제는 CheckClear(), 연한 구역 탐색은 FindDelete()
    while True:
        # 만약에 줄이 사라지지 않고, 연한 구역에 블록이 없으면 Break
        if CheckClear() == False and FindDelete() == False:
            break
        # 블록이 사라져서 블록의 이동이 필요할 경우 MoveBlock() 수행
        MoveBlock()


n = int(input())
q = deque()
for i in range(n):
    q.append(list(map(int, input().split())))

green = [[0] * 4 for _ in range(6)]
blue = [[0] * 6 for _ in range(4)]
ans = 0
index = 1

while q:
    go(q.popleft(), index)
    index += 1

def countBlock():
    global green, blue
    count = 0
    for i in range(5, 1, -1):
        for j in range(4):
            if green[i][j] > 0:
                count += 1
    for i in range(4):
        for j in range(2, 6):
            if blue[i][j] > 0:
                count += 1

    return count

print(ans)
print(countBlock())