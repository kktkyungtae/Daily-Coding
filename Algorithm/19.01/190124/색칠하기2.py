
import sys

sys.stdin = open("sample_input.txt", "r")


tc = int(input())

def get_max(lists,max_num):
    for i in range(len(lists)):
        if max_num<lists[i] :
            max_num =lists[i]
            return max_num

for i in range(tc):
    n = int(input())#입력받는 도형의 개수
    result = 0
    square_num_lists = []

for a in range(n):
    square_num_lists.append(list(map(int,input().split())))
    max_num = 0

for a in range(n):#최대값을 구한다.
    max_num = get_max(square_num_lists[a],max_num)

    result_lists = [[0]*(max_num+1) for a in range(max_num+1)]


for a in range(n):
    if square_num_lists[a][-1]==1:
    for b in range(square_num_lists[a][0],square_num_lists[a][2]+1):
    for c in range(square_num_lists[a][1],square_num_lists[a][3]+1):
    result_lists[b][c]+=1
    else:
    for b in range(square_num_lists[a][0],square_num_lists[a][2]+1):
    for c in range(square_num_lists[a][1],square_num_lists[a][3]+1):
    result_lists[b][c]+=2
    cnt = 0
    for a in range(len(result_lists)):
for b in range(len(result_lists[a])):
if result_lists[a][b]==3:
cnt+=1

print(f"#{i+1} {cnt}")