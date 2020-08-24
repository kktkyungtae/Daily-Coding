class Node:
    def __init__(self, data, link):
        self.data = data
        self.link = link

def get(index):
    node = Head
    for i in range(index):
        node = node.link

    return node


T = int(input())

for t in range(T):
    N, M = map(int, input().split())
    li_N = []

    for m in range(M):
        li_N.append(list(map(int, input().split())))

    Head = Node(li_N[0][N - 1], None)

    for i in range(N - 2, -1, -1):
        Head = Node(li_N[0][i], Head)

    node = None

    for i in range(1, M):
        for j in range(i * N):
            node = get(j)
            if li_N[i][0] < get(j).data:
                if j == 0:
                    for q in range(N-1, -1, -1):
                        Head = Node(li_N[i][q], Head)
                    break
                else:
                    node = get(j - 1)
                    for q in range(N):
                        new_node = Node(li_N[i][q], node.link)
                        node.link = new_node
                        node = new_node
                    break
            elif j == (i*N)-1:
                for q in range(N):
                    new_node = Node(li_N[i][q], node.link)
                    node.link = new_node
                    node = new_node
                break

    result = ""

    for i in range(N * M - 1, N * M - 11, -1):
        result += f"{get(i).data} "

    print(f"#{t + 1} {result}")