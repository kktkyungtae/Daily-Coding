# 두 줄에 걸쳐서 단어가 주어진다
# 두 단어를 같게 하기 위해서 제거해야하는 최소의 문자수를 구하라

from collections import Counter
s1 = input()
s2 = input()

a = Counter(s1)
b = Counter(s2)
answer = 0
print(a)
print(b)
print()
print((a-b))
print((b-a))
print(((a-b) + (b-a)).values())
for v in ((a-b) + (b-a)).values() :
    answer += v
print(answer)