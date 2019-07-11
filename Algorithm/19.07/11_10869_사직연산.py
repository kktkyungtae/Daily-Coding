import sys
sys.stdin=open('11_10869.txt','r')

V,E = map(int,input().split())

print(V+E)
print(V-E)
print(V*E)
print(V//E)
print(V%E)