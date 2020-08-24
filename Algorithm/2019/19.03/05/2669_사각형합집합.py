import sys
sys.stdin = open('2669_input.txt','r')

rect_list = []

for j in range(4):
    in_ = list(map(int, input().split()))
    rect_list.append(in_)

# # 전체 합
# for i in range(len(rect_list)):
#     total += (rect_list[i][2] - rect_list[i][0]) * (rect_list[i][3] - rect_list[i][1])
#
# for o in range(5):

mat = [[0] * 10 for i in range(10)]
for q in range(4):
    for i in range(rect_list[q][1], rect_list[q][3]):  # y
        for j in range(rect_list[q][0], rect_list[q][2]):  # x
            if mat[i][j] == 0:
                mat[i][j] = 1

cnt = 0
for i in range(10):
    for j in range(10):
        if mat[i][j] == 1:
            cnt += 1

print(cnt)




