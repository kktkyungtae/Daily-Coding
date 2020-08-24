T = int(input())

for t in range(T):
    N, M = map(int, input().split())
    queue = [0] * N
    front = rear = 0

    li_N = list(map(int, input().split()))
    for i in range(len(li_N)):
        queue[i] = li_N[i]
        rear = (rear + 1) % len(queue)

    for i in range(M):
        front = (front + 1) % len(queue)
        a = queue[front]

        rear = (rear + 1) % len(queue)
        queue[rear] = a

    print(f"#{t+1} {queue[front]}")