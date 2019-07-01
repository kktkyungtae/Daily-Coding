import sys
sys.stdin = open('12_input.txt')

for tc in range(10):
    n = input()
    ladder_lists = [[] for a in range(100)]
    for a in range(100):
        ladder_lists[a] = list(map(int, input().split()))

    cnt = 0
    while ladder_lists[99][cnt] != 2:  # 골인지점 찾기
        cnt += 1

    # 초기 x,y좌표
    x = 99
    y = cnt

    while x != 0:
        if y != 0 and y != 99:  # 양 끝이 아니라면
            if ladder_lists[x][y - 1] == 1:  # 왼쪽 체크
                while ladder_lists[x][y - 1] == 1:
                    y -= 1
                    if y == 0:  # 왼쪽 끝일경우 그만
                        break
                x -= 1
            elif ladder_lists[x][y + 1] == 1:  # 오른쪽 체크
                while ladder_lists[x][y + 1] == 1:
                    y += 1
                    if y == 99:  # 오른쪽 끝일경우 그만
                        break
                x -= 1
            elif ladder_lists[x - 1][y] == 1:  # 그냥 else로 해도됨
                x -= 1

        elif y == 0:
            if ladder_lists[x][y + 1] == 1:  # 오른쪽만 체크
                while ladder_lists[x][y + 1] == 1:
                    y += 1
                    if y == 99:
                        break
                x -= 1
            elif ladder_lists[x - 1][y] == 1:
                x -= 1

        elif y == 99:
            if ladder_lists[x][y - 1] == 1:  # 왼쪽만 체크
                while ladder_lists[x][y - 1] == 1:
                    y -= 1
                    if y == 0:
                        break
                x -= 1
            elif ladder_lists[x - 1][y] == 1:
                x -= 1

    print("#{} {}".format(n,y))