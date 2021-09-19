# https://www.acmicpc.net/problem/17136

# 1. a에 종이의 상태를 저장하고 paper에 다섯 종류의 색종이를 각각 몇 장 사용했는지 저장한다
# 2. (0, 0)부터 시작해서 a[x][y]가 1인 모든 좌표에서 크기 1~5인 색종이를 붙여가면서 모든 케이스를 확인해야 한다
# 3. x좌표가 범위를 넘어가면 (0, y+1)로 재귀한다
#    y가 범위를 넘어가면 맨 끝까지 탐색한 것이므로 최소값을 갱신한다
# 4. a[x][y]가 0이면 (x+1, y)로 재귀한다
#    1이면 크기 1부터 5까지 색종이를 붙일 수 있는지 확인한다
# 5. 만약 색종이 5장을 이미 붙였거나 범위를 벗어나는 크기의 색종이라면 continue한다
# 6. 색종이를 붙일 수 있는지 확인한다. 단순히 반복문으로 0이 있는지 검사하면 된다
# 7. 붙일 수 있으면 다시 반복문으로 색종이를 붙이는 칸의 숫자를 0으로 바꿔준다
# 8. paper를 증가시켜 주고 (x+k+1, y)로 재귀한다
#    그다음에는 paper와 지운 칸을 다시 되돌려준다

def func(x, y, cnt):
    global ans
    # y가 범위를 넘어가면, 끝까지 탐색했다는 뜻
    if y >= 10:
        ans = min(ans, cnt)
        return

    # x가 범위를 넘어가면, y + 1로 재귀돌린다
    if x >= 10:
        func(0, y+1, cnt)
        return

    if mapp[x][y] == 1:
        for k in range(5):
            # 종이를 5개 다 썼으면! continue
            if paper[k] == 5:
                continue
            # 종이 붙였을 때 범위를 벗어나면! continue
            if x + k >= 10 or y + k >= 10:
                continue

            # 색종이를 붙일 수 있는지 확인
            flag = 0
            for i in range(x, x + k + 1):
                for j in range(y, y + k + 1):
                    # 색종이를 붙인 범위 안에 0이 있으면 break!
                    if mapp[i][j] == 0:
                        flag = 1
                        break
                # 오호! flag를 활용해서 2중 for문 break
                if flag == 1:
                    break

            # 색종이를 붙일 수 있으니까, 붙인 범위는 모두 0으로
            if flag == 0:
                for i in range(x, x + k + 1):
                    for j in range(y, y + k + 1):
                        mapp[i][j] = 0

                # 쓴 종이 +1
                paper[k] += 1
                # 붙이고난 좌표부터 다시 재귀
                func(x + k + 1, y, cnt + 1)
                # 재 탐색을 위해 되돌림..??
                paper[k] -= 1

                # 바뀐 좌표들을 다시 1로 바꿔줌
                for i in range(x, x + k + 1):
                    for j in range(y, y + k + 1):
                        mapp[i][j] = 1
    else:
        func(x + 1, y, cnt)

mapp = []
for _ in range(10):
    mapp.append(list(map(int, input().split())))

paper = [0 for _ in range(5)]
ans = 1e9
func(0,0,0)

if ans != 1e9:
    print(ans)
else:
    print(-1)
