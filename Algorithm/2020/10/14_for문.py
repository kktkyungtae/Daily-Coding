n = [1,1,1,1,1,[1,2]]

# visited = [False, False .. ] 만들기
visited = [False] * len(n)
print(visited)

visited2 = [[False] for i in range(len(n))]
print(visited2)

visited3 = [[False] for _ in range(len(n))] * 2
print(visited3)

visited4 = [[False] * 5 for _ in range(5)]
print(visited4)

k = 3
graph = []
for i in range(k):
    graph.append(list(map(int, input())))

gvisited = [[False] * 4 for _ in range(k)]
print(graph)
print(gvisited)