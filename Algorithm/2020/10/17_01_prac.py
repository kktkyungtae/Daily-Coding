import sys

input = sys.stdin.readline


def findDelete():
    global green, blue
    countGreen = 0;
    countBlue = 0;
    # 초록판의 연한부분의 첫번째 줄 탐색
    for i in range(4):
        # 해당 줄에 블록이 하나라도 존재하면 나머지 부분은 탐색하지 않아도 됩니다.
        if green[0][i] > 0: countGreen += 1; break;
    # 초록판의 연한부분의 두번째 줄 탐색
    for i in range(4):
        if green[1][i] > 0:
            countGreen += 1
            break

    # 파란판의 연한부분 탐색
    for i in range(4):
        if blue[i][0] > 0: countBlue += 1; break;
    for i in range(4):
        if blue[i][1] > 0: countBlue += 1; break;

    # 연한부분에 있던 줄 수만큼 바닥의 줄을 지워줍니다.
    for i in range(countGreen):
        for j in range(4):
            green[5 - i][j] = 0
    for i in range(4):
        for j in range(countBlue):
            blue[i][5 - j] = 0

    # 연한부분에 블록이 존재했는지 아닌지를 반환합니다.
    if countGreen == 0 and countBlue == 0:
        return False
    else:
        return True


# moveBlock()에서 블록이 다중블록 (2*1, 1*2) 라면 그 인접 블록의 좌표도 찾아주는 함수입니다.
def findMultipleBlockState(i, j, value, isGreen):
    global green, blue
    result = []
    result.append([i, j])
    directions = (1, 0), (0, 1), (-1, 0), (0, -1)
    for dx, dy in directions:
        if isGreen and 0 <= i + dx < 6 and 0 <= j + dy < 4 and green[i + dx][j + dy] == value: result.append(
            [i + dx, j + dy]); break
        if not isGreen and 0 <= i + dx < 4 and 0 <= j + dy < 6 and blue[i + dx][j + dy] == value: result.append(
            [i + dx, j + dy]); break
    return result


# 실질적으로 블록을 이동시켜주는 함수입니다. 1*1 뿐만 아니라 1*2, 2*1 블록도 같이 이동시켜주게 구현하였습니다.
def move(blockstate, value, isGreen):
    global green, blue
    nowx, nowy = blockstate[0]
    nearx, neary = (-1, -1)
    if len(blockstate) == 2: nearx, neary = blockstate[1]
    if isGreen:
        while True:
            nextx = nowx + 1
            if nearx != -1: nextnearx = nearx + 1
            if nextx >= 6 or green[nextx][nowy] > 0: break
            if nearx != -1 and green[nextnearx][neary] > 0 and green[nextnearx][neary] != value: break
            green[nextx][nowy] = value;
            green[nowx][nowy] = 0;
            nowx = nextx
            if nearx != -1: green[nextnearx][neary] = value; green[nearx][neary] = 0; nearx = nextnearx
    else:
        while True:
            nexty = nowy + 1
            if neary != -1: nextneary = neary + 1
            if nexty >= 6 or blue[nowx][nexty] > 0: break
            if neary != -1 and blue[nearx][nextneary] > 0 and blue[nearx][nextneary] != value: break
            blue[nowx][nexty] = value;
            blue[nowx][nowy] = 0;
            nowy = nexty
            if neary != -1: blue[nearx][nextneary] = value; blue[nearx][neary] = 0; neary = nextneary

        # 이동할 블럭을 탐색해주는 함수입니다.


# go()상단에는 생성된 블록만 움직였지만 moveBlock()에서는 바닥부분을 제외한 모든 칸을 탐색합니다.(바닥부분은 이동이 불필요하므로)
def moveBlock():
    global green, blue
    for i in range(1, 6):
        for j in range(4):
            # 초록부분 입니다.
            if green[5 - i][j] > 0:
                # 블록이 있는 경우 먼저 이 블록이 1*1 블록이 아닌지를 체크합니다.
                blockstate = findMultipleBlockState(5 - i, j, green[5 - i][j], True)
                # 블록을 움직여주는 move()함수에 정보를 담아 보내줍니다.
                move(blockstate, green[5 - i][j], True)
                # 파랑부분 입니다.
            if blue[j][5 - i] > 0:
                blockstate = findMultipleBlockState(j, 5 - i, blue[j][5 - i], False)
                move(blockstate, blue[j][5 - i], False)

            # 블록의 이동 후 항상 확인해주는 메소드입니다. 한 row 혹은 col에 값이 모두 채워져 있을 경우 점수를 올리고 해당 줄을 지웁니다.


def checkClear():
    global green, blue, answer
    resultg = [];
    resultb = []

    # 초록판 부분입니다.
    for i in range(4):
        count = 0
        for j in range(4):
            # 칸이 0인경우 count변수에 -1을, 0아 아닌경우(블록이 있는경우) +1을 저장시킵니다.
            # 종료조건을 주기 위해 블록의 가장 바닥부분부터 탐색합니다.
            if green[5 - i][j] == 0:
                count -= 1
            else:
                count += 1
        # 해당 줄이 모두 0인 경우 (즉, 비어있는 경우) 그 다음 줄은 당연히 블록이 없으므로 (중력에 의해) 반복문을 종료시켜줍니다.
        if count == -4:
            break
        # 해당 줄이 꽉 채워져있으면 해당 줄 index를 저장시킵니다.
        elif count == 4:
            resultg.append(5 - i)

    # 파랑 판 부분입니다.
    for i in range(4):
        count = 0
        for j in range(4):
            if blue[j][5 - i] == 0:
                count -= 1
            else:
                count += 1
        if count == -4:
            break
        elif count == 4:
            resultb.append(5 - i)

        # 위에서 저장된 줄 index가 존재할 경우 해당 줄을 모두 0으로 바꿔주며 점수를 1점 올려줍니다.
    if len(resultg) > 0:
        for gx in resultg:
            answer += 1
            for j in range(4):
                green[gx][j] = 0
    if len(resultb) > 0:
        for by in resultb:
            answer += 1
            for i in range(4):
                blue[i][by] = 0

                # 줄이 사라졌는지 안사라졌는지를 체크하기 위해 결과를 반환합니다.
    if len(resultg) > 0 or len(resultb) > 0:
        return True
    else:
        return False


# Main의 마지막 부분에서 그리드에 남은 블록 수를 출력하기 위해 이를 계산해주는 함수입니다.
def countBlock():
    global green, blue
    count = 0
    for i in range(6):
        for j in range(6):
            if i <= 3 and blue[i][j] > 0: count += 1
            if j <= 3 and green[i][j] > 0: count += 1
    return count


# Main에서 호출하는 첫번째 함수입니다.
def go(param, index):
    global answer
    t, x, y = param
    # 먼저 받아낸 좌표값과 블록 모형을 Green, Blue에 각각 생성해줍니다.
    if t == 1:
        green[0][y] = index
        blue[x][0] = index
    elif t == 2:
        green[0][y] = index; green[0][y + 1] = index
        blue[x][0] = index; blue[x][1] = index
    else:
        green[0][y] = index; green[1][y] = index
        blue[x][0] = index
        blue[x + 1][0] = index
    nowx = 0
    nowy = 0

    # 위에서 생성된 블록을 벽이나 다른 블록에 부딛힐 때까지 움직입니다.
    # moveBlock() 함수를 호출해주는 것 보다 해당 로직을 다시한번 쓰는게 코드는 길어지더라도
    # 시간은 짧아질 것 같아 굳이 한번 더 썼습니다. (탐색을 수행하지 않아도되므로)
    if t == 1:
        # move green
        while True:
            nextx = nowx + 1
            if nextx >= 6 or green[nextx][y] != 0: break
            green[nextx][y] = green[nowx][y];
            green[nowx][y] = 0;
            nowx = nextx
            # move blue
        while True:
            nexty = nowy + 1
            if nexty >= 6 or blue[x][nexty] != 0: break
            blue[x][nexty] = blue[x][nowy];
            blue[x][nowy] = 0;
            nowy = nexty
    elif t == 3:
        # move green
        nowx = 1
        while True:
            nextx = nowx + 1
            if nextx >= 6 or green[nextx][y] != 0: break
            green[nextx][y] = green[nowx][y];
            green[nowx - 1][y] = 0;
            nowx = nextx
        # move blue
        while True:
            nexty = nowy + 1
            if nexty >= 6 or blue[x][nexty] != 0 or blue[x + 1][nexty] != 0: break
            blue[x][nexty] = blue[x][nowy];
            blue[x + 1][nexty] = blue[x + 1][nowy];
            blue[x][nowy] = 0;
            blue[x + 1][nowy] = 0;
            nowy = nexty
    else:
        # move green
        while True:
            nextx = nowx + 1
            if nextx >= 6 or green[nextx][y] != 0 or green[nextx][y + 1] != 0: break
            green[nextx][y] = green[nowx][y];
            green[nextx][y + 1] = green[nowx][y + 1];
            green[nowx][y] = 0;
            green[nowx][y + 1] = 0;
            nowx = nextx
        nowy = 1
        # move blue
        while True:
            nexty = nowy + 1
            if nexty >= 6 or blue[x][nexty] != 0: break
            blue[x][nexty] = blue[x][nowy];
            blue[x][nowy - 1] = 0;
            nowy = nexty

            # 이후 줄이 사라지거나 연한 그리드에 블록이 있을 경우 행을 삭제해주고 점수를 올려주는 방법을 반복합니다.
    # 점수계산과 줄의 삭제는 checkClear() 메소드에서, 연한부분의 탐색은 findDelete()에서 수행해줍니다.
    while True:
        # 만약 줄이 사라지지 않았고 연한 그리드에도 블록이 없으면 움직임을 종료합니다.
        if checkClear() == False and findDelete() == False: break
        # 줄이 사라져 블록의 이동이 필요할 경우 moveBlock()이 이를 수행해줍니다.
        moveBlock()


# Main 입니다.
n = int(input())
# 입력값을 큐에 넣어 차례대로 돌립니다.
qu = []
for i in range(n):
    qu.append(list(map(int, input().split())))
green = [[0 for _ in range(4)] for _ in range(6)]
blue = [[0 for _ in range(6)] for _ in range(4)]
answer = 0;
index = 1
while qu:
    go(qu.pop(0), index)
    index += 1
print(answer)
print(countBlock())