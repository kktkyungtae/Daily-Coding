def recursive_fuction(i):
    if i == 10:
        return
    else:
        print(i, '번째 재귀함수에서', i+1, '번째 재귀함수를 호출하여라!')
        recursive_fuction(i+1)
        print(i, '번째 재귀함수를 종료합니다.')

recursive_fuction(1)