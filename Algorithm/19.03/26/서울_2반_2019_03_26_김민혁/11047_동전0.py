N , donmana = map(int,input().split())

dondon = []
for i in range(N):
    don = int(input())
    dondon.append(don)

D = dondon[::-1]
count = 0
while(1):
    for i in range(N):
        if donmana - D[i] >= 0:
            donmana = donmana -D[i]
            count += 1 
            break 
        
    if donmana == 0:
        break 

print(count)

        

    
    