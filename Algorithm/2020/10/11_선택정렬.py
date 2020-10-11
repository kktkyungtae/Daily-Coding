a = [7, 5, 8 , 9, 0, 2, 1, 3, 4, 6]

# 전체 열의 마지막 앞까지만 진행
for i in range(len(a)):
    min_index = i # 가장 작은 원소의 인덱스 // 일단 첫! index

    # 가장 작은 값의 index를 찾는 for문
    for j in range(i+1, len(a)):
        if a[min_index] > a[j]:
            min_index = j

    # 두 원소의 위치를 바꾸는 스와프
    a[i], a[min_index] = a[min_index], a[i]

print(a)