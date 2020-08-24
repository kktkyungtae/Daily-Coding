import sys

sys.stdin = open("sample_input.txt", "r")

tc = int(input())

for i in range(tc):
    p,a,b= map(int,input().split())#책의 전체 쪽 수 p,a가 찾을 쪽수a,b가 찾을 쪽수b
    result = 0# #출력은 A B 0중 하나0
    judge_flag = 0

    l=1
    r=p

cnt_a = 0
cnt_b = 0
while True:
c = int((l + r) / 2)
cnt_a+=1
if c<a:
l = c
elif c>a:
r = c
else :
break
if l>=r:
judge_flag=1
break
l=1
r=p
while True:
c = int((l + r) / 2)
cnt_b += 1
if c < b:
l = c
elif c > b:
r = c
else:
break
if cnt_a<cnt_b:
print(f"#{i + 1} A")
elif cnt_b < cnt_a:
print(f"#{i + 1} B")
else :
print(f"#{i + 1} 0")