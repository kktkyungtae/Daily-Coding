n,k = map(int,input().split())
w = []
v = []
for _ in range(n):
    W,V = map(int,input().split())
    w.append(W)
    v.append(V)
d = [0]*(k+1)
for i in range(n):
    for j in range(k,0,-1):
        if j-w[i]>=0:
            d[j] = max(d[j],d[j-w[i]]+v[i])

print(d[k])