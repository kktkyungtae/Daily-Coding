class Node:
    def __init__(self, data, link):
        self.data = data
        self.link = link


def add(pre, data):
    pre.link = Node(data, pre.link)


def get(index):
    node = Head

    for i in range(index):
        node = node.link

    return node


T = int(input())

for t in range(T):
    N, M, L = map(int, input().split())
    li_N = list(map(int, input().split()))

    Head = Node(li_N[N - 1], None)

    for i in range(N - 2, -1, -1):
        Head = Node(li_N[i], Head)

    for m in range(M):
        pre, data = map(int, input().split())
        add(get(pre - 1), data)

    print(f"#{t + 1} {get(L).data}")