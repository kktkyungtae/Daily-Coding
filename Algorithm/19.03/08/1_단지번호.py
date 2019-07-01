import sys
sys.stdin = open('1_input','r')

S = int(input())

all_danji = []
for i in range(S):
    danji = list(input())
    all_danji.append(danji)

visited = [[False]*S for _ in range(S)]
# for j in range(S):
#     visited.append([False for i in range(S)])

dx = [1,-1,0,0]
dy = [0,0,1,-1]

# visited True check
for i in range(S):
    for j in range(S):
        if all_danji[i][j] == '0':
            visited[i][j] = True

result_li= []
for i in range(S):
    for j in range(S):
        if visited[i][j] == False:
            stack = []
            stack.append([i,j])
            visited[i][j] = True


            cnt = 1
            while stack:
                temp = stack.pop()

                for k in range(4):
                    temp_x = temp[0] + dx[k]
                    temp_y = temp[1] + dy[k]

                    if 0 <= temp_x < S and 0 <= temp_y < S:
                        if visited[temp_x][temp_y] == False:
                            stack.append([temp_x,temp_y])
                            visited[temp_x][temp_y] = True
                            cnt+=1
            result_li.append(cnt)

print('{}'.format(len(result_li)))
result_li.sort()
for i in result_li:
    print(i)

                        
                        
                        
                        




