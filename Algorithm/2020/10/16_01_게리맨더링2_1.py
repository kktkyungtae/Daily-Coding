import sys

input = sys.stdin.readline

def divide(x, y, d1, d2, ans):
    # 어찌보면 for문 보다 while이 더 좋을 수도 있다.
    # 상황에 맞게 잘 써야 하는데..
    while True:
        while True:
            # 왼쪽 좌표
            lx, ly = x + d1, y - d1
            # 오른쪽 좌표
            rx, ry = x + d2, y + d2
            # 아래쪽 좌표
            bx, by = x + d1 + d2, y - d1 + d2

            # 범위를 벗어나면!
            if lx == n-1 or ly == 0:
                break
            if rx == n-1 or ry == n-1:
                break
            if bx >= n or by >= n or by < 0:
                break

            # 범위 내라면
            # 각 선거구의 인구수를 구한다!
            ans = min(ans, find_min(x, y, lx, ly, rx, ry, by))
            # d2를 +1 해가며 가능한 범위 내에 모두 검증
            d2 += 1
        # 가능한 범위내 d2가 검증 다 되면, d1도 +1 해서 검증
        d1 += 1
        if x + d1 == n-1 or y - d1 == -1:
            break
        d2 = 1

    return ans

def find_min(x, y, lx, ly, rx, ry, by):
    cnt1, cnt2, cnt3, cnt4, d = 0, 0, 0, 0, 0

    # 첫번째 선거구
    # x 범위는 왼쪽 x좌표, y 범위는 기준좌표의 y값
    for i in range(lx):
        for j in range(y+1):
            # 인덱스가 기준점과 같아지면
            if [i, j] == [x + d, y - d]:
                d += 1
                break
            cnt1 += mapp[i][j]

    d = 1
    # 여기는 왜 rx + 1이게! 그림 보니까 2번은 rx 옆자리에 있을 수 있음!
    for i in range(rx+1):
        for j in range(n-1, y, -1):
            # 어짜피 range가 y면 y-1까지 밖에 못가니까
            if [i, j] == [x + d, y + d]:
                d += 1
                break
            cnt2 += mapp[i][j]

    d = 0
    for i in range(lx, n):
        for j in range(by):
            if [i, j] == [lx + d, ly + d]:
                d += 1
                break
            cnt3 += mapp[i][j]

    d = 1
    for i in range(rx+1, n):
        for j in range(n-1, by-1, -1):
            if [i, j] == [rx + d, ry - d]:
                d += 1
                break
            cnt4 += mapp[i][j]

    cnt5 = nsum - cnt1 - cnt2 - cnt3 - cnt4
    max_cnt = max(cnt1, cnt2, cnt3, cnt4, cnt5)
    min_cnt = min(cnt1, cnt2, cnt3, cnt4, cnt5)
    return max_cnt - min_cnt

n = int(input())

mapp, nsum = [], 0
# 입력과 동시에, 원래 인구 총합을 구해 놓는다! 1,2,3,4 구역을 구해서 빼면 5구역 나오니깐
for _ in range(n):
    row = list(map(int, input().split()))
    nsum += sum(row)
    mapp.append(row)

ans = 10e9
# 기준점은 x는 0부터 n-2까지 가능하고, y축은 1에서 n-1까지 가능
# 이 범위 내에 모든 경우의 수를 다 해보자
for i in range(n-2):
    for j in range(1, n-1):
        # 처음에 d1, d2는 1로 설정
        d1, d2 = 1, 1
        # 해당 범위 안에서 모든 경우의 수를 확인하는 divide
        ans = divide(i, j, d1, d2, ans)
print(ans)