import numpy as np

list_data = [1,2,3]

# numpy 자료형으로 바꾸는 것
array = np.array(list_data)

print(array)

# array는 numpy 데이터이기 때문에
# size(갯수)와 dtype(데이터 타입)등 함수가 제공된다

print(array.dtype)
print(array.size)

# numpy도 인덱스와 같이 특정 어래이에 접근이 가능하다
print(array[1])