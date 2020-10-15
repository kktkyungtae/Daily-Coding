from collections import Counter
import itertools

a = [1,1,1,1,2,3,4,4,4,5]
b = [2,2,4,4]

c = Counter(a)
d = Counter(b)

print(c)
# 정렬!!
cc1 = sorted(c.items(), key=lambda x:x[0])
cc2 = sorted(c.items(), key=lambda x:x[0], reverse=True)
print(cc1)
print(cc2)
print("가장 많이 등장한 놈 뽑기") # 등등 인덱스 슬라이싱도 된다
print(cc1[0])


ff1 = sorted(c.items(), key=lambda x:x[1])
ff2 = sorted(c.items(), key=lambda x:x[1], reverse=True)
print(ff1)
print(ff2)

print()
print('###########################################')

bb = {'A':3, 'C':1, 'G':5, 'T':2}
print(bb)

# 리스트 객체로 만들기
kk = bb.items()
print(kk)
k = sorted(kk, key=lambda x:x[1])
print(k)