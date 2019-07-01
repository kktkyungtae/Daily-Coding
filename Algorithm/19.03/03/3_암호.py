class Node:
    def __init__(self, data, link):
        self.data = data
        self.link = link

def get(index):
    node = Head
    for x in range(index):
        node = node.link

    return node.data

T = int(input())

for t in range(T):
    N, M, K = map(int, input().split())
    temp_li = list(map(int, input().split()))

    Head = Node(temp_li[N - 1], None)
    top = Head

    for i in range(N - 2, -1, -1):
        Head = Node(temp_li[i], Head)

    top.link = Head

    node = Head
    for k in range(K):
        for m in range(M - 1):
            node = node.link
        new_node = Node(node.data + node.link.data, node.link)
        node.link = new_node
        node = new_node

    if N + K < 10:
        print(f"#{t + 1}", end=" ")
        for i in range(N+K-1, -1, -1):
            print(get(i), end=" ")
    else:
        print(f"#{t + 1}", end=" ")
        for i in range(N+K-1, N+K-11, -1):
            print(get(i), end=" ")
    print("")