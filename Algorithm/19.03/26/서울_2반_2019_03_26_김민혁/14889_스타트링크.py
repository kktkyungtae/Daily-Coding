# 못풀었습니다 죄송합니다 ㅜㅜㅜ
# 못풀었습니다 죄송합니다 ㅜㅜㅜ
# 못풀었습니다 죄송합니다 ㅜㅜㅜ 


T = int(input())
ma = []
for test in range(T):
    num = list(map(int,input().split()))
    ma.append(num)

numlist = []
for i in range(0,T):
    for j in range(i+1,T):
        numlist.append(ma[i][j]+ma[j][i])

print(numlist)



    


        
        

