import sys
sys.stdin=open('1244_input.txt','r')

N = int(input())
# def mans(switch):
#     k = member[i][0]
#     for i in range(0,len(switch),k):
#         if switch[i] == 0:
#             switch[i] = 1
#         else:
#             switch[i] = 0
#
#
# def womans(swith):





switch = list(map(int,input().split()))
switch.insert(0,0)

people = int(input())
member = []
for p in range(people):
    temp = list(map(int,input().split()))
    member.append(temp)
print(switch)
for i in range(people):
    if member[i][0] == 1:
        k = member[i][1]
        for i in range(k,len(switch),k):
            if switch[i] == 0:
                switch[i] = 1
            else:
                switch[i] = 0
    else:

