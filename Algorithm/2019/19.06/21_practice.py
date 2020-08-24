from collections import deque

# 2차 배열을 쉽게
def asdf(array):
    return [print(*i) for i in array]


# itertools
from itertools import combinations, permutations

a = [1,2,3,4,5]

for combi in combinations(a,3):
    print(combi)

for permi in permutations(a,3):
    print(permi)

# product

for tc in range(int(input())):
    n=int(input())
    ans=0
    mat=[list(map(int, input().split())) for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if mat[i][j]==1:
                mat[i][j]=0
                hi=deque()
                hi.append((i,j))
                while hi:
                    x,y = hi.pop()
                    for dx,dy in (1,0),(-1,0),(0,1),(0,-1):
                        nx,ny=x+dx,y+dy
                        if 0<=nx<n and 0<=ny<n and mat[nx][ny]==1:
                            mat[nx][ny]=0
                            hi.append((nx,ny))
                    if len(hi)==0:
                        ans+=1
    print("#{} {}".format(tc+1, ans))


b=range(100)
for i in b:
    print(i)
# 행렬 변경
test = [
    [3,3,3,3,3,3],
    [5,5,5,5,5,5]
]


asdf(zip(*test))

a=[1,2,3,4,5,6,7]
a=set(a)

# 미세먼지
# 낚시왕
# 연구소
# 색종이 붙이기
# 캐슬디펜스
# 17281 : 야구공
# 아기상어2
# 파이프 옮기기