Meet_n = int(input())
meet = []
for ms in range(Meet_n):
    s, e = map(int,input().split())
    meet.append([e,s])

time_s = [[0,0]]

#must have sort
meet.sort()

for i in range(len(meet)):
    if time_s[-1][0] <= meet[i][1]:
        time_s.append(meet[i])

print(len(time_s)-1)