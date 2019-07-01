
# 한 개의 회의실이 있는데 이를 사용하고자 하는 N개의 회의들에 대하여 
# 회의실 사용표를 만들려고 한다. 각 회의 I에 대해 시작시간과 끝나는 
# 시간이 주어져 있고, 각 회의가 겹치지 않게 하면서 회의실을 사용할 수 있는 
# 최대수의 회의를 찾아라. 
# 단, 회의는 한번 시작하면 중간에 중단될 수 없으며 한 회의가 끝나는 것과 동시에
# 다음 회의가 시작될 수 있다. 회의의 시작시간과 끝나는 시간이 같을 수도 있다. 
# 이 경우에는 시작하자마자 끝나는 것으로 생각하면 된다.

T = int(input())
N = []
for test in range(T):
    S,E = map(int,input().split())
    N.append([E,S])

N = sorted(N) 
start = N[0][0] #end  
count = 1

for i in range(1,len(N)):
    if N[i][1] >= start:# 다음에 올 start가 이전의 end보다 크거나 같으면  
        start = N[i][0] # 변수를 현재 end값으로 갱신하고 
        count += 1  # 카운트를 해준다. 

print(count)