T = int(input())
A = list(map(int,input().split()))

A = sorted(A)

result = 0
for i in range(T+1):
    for j in range(0,i): 
        result += A[j]
print(result)
        

