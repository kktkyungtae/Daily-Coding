class Node:
    def __init__(self, data, link):
        self.data = data
        self.link = link

def add(pre, data):
    pre.link = Node(data, pre.link)

def get(index):
    node = Head
    try:
        for i in range(index):
            node = node.link

        return node
    except:
        return Node(-1, None)

def delete(pre):
    pre.link = pre.link.link


T = int(input())

for t in range(T):
    N, M, L = map(int, input().split())
    li_N = list(map(int, input().split()))

    Head = Node(li_N[N - 1], None)

    for i in range(N - 2, -1, -1):
        Head = Node(li_N[i], Head)

    for m in range(M):
        msg = input().split()
        activity = msg.pop(0)

        if activity == 'I':
            pre, data = map(int, msg)
            add(get(pre - 1), data)

        elif activity == 'D':
            pre = int(msg[0])
            delete(get(pre - 1))

        elif activity == 'C':
            pre, data = map(int, msg)
            delete(get(pre - 1))
            add(get(pre - 1), data)

    print(f"#{t + 1} {get(L).data}")