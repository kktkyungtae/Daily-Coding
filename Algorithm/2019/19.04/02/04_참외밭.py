import sys
sys.stdin = open('04_input.txt','r')

C = int(input())

bat = []
bat_shift = []
bat_width = []
for i in range(6):
    temp_bat = list(map(int,input().split()))
    bat.append(temp_bat)

for j in range(len(bat)):
    bat_shift.append(bat[j][0])
    bat_width.append(bat[j][1])

