# 주어진 2차원 배열에서
# 1은 칸막이 이고, 0은 비어있는 공간이다
# 비어있는 공간에 아이스크림을 부어서 만들 수 있는 덩어리를 구하라
############################
# 연결된 컴포넌트를 찾는 문제
############################

s, g = map(int, input().split())
mapp = []
for i in range(s):
    # 공백없는 숫자를 받을 때
    mapp.append(list(map(int, input())))

# DFS 특정 노드를 방문하고 연결된 모든 노드들도 방문
def dfs(x, y):
    if x <= -1 or x >= s or y <= -1 or y >=g:
        return False

    if mapp[x][y] == 0:
        # 방문하지 않았다면, 방문처리하고
        mapp[x][y] = 1

        #상하좌우 위치들도 모두 재귀적으로 호출
        dfs(x - 1, y)
        dfs(x + 1, y)
        dfs(x, y - 1)
        dfs(x, y + 1)
        return True
    return False

result = 0
for i in range(s):
    for j in range(g):
        if dfs(i, j) == True:
            # DFS 수행되면, 한 구역 돈거니까 +1 해주는 것
            result += 1

print(result)

# 4 5
# 00110
# 00011
# 11111
# 00000