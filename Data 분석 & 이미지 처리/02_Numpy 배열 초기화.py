import numpy as np

# 실제로 데이터 분석과 관련한 데이터 분석을 할 떄는
# 다양한 연산을 지원해주는 기능이 필요하다
# numpy에 있다!

# 0 부터 3까지의 배열 만들기
array1 = np.arange(4)
print(array1)

# 데이터를 만드는데, 각 0으로 초기화해서 만들기 //
# 0으로 구성된 4x4 형태의 type에 맞게 만들어줌
array2 = np.zeros((4,4), dtype=float)
print(array2)

array2 = np.ones((4,2), dtype=str)
print(array2)

# 0부터 9까지 랜덤하게 초기화 된 배열 만들기
array4 = np