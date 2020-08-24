def check(li):
    check_li = [0] * 10
    for item in li:
        for x in range(1, 10):
            if item == x:
                if check_li[x] == 1:
                    return False
                check_li[x] = 1
                break
    return True


T = int(input())

for t in range(T):
    sudoku = []
    for i in range(9):
        sudoku.append(list(map(int, input().split())))

    result = 1

    # 가로 탐색
    for i in range(9):
        if not check(sudoku[i]):
            result = 0
            break

    # 행렬 전치
    for i in range(9):
        for j in range(9):
            if i < j:
                sudoku[i][j], sudoku[j][i] = sudoku[j][i], sudoku[i][j]

    # 세로 탐색
    for i in range(9):
        if not check(sudoku[i]):
            result = 0
            break

    # 네모 탐색
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            square = []
            for q in range(3):
                for p in range(3):
                    square.append(sudoku[i + q][j + p])
            if not check(square):
                result = 0

    print(f"#{t + 1} {result}")