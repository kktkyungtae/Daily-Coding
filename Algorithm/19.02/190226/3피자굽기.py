def all_done(queue):
    for q in queue:
        if q[0] == -1 and q[1] == -1:
            pass
        else:
            return False
    return True


T = int(input())

for t in range(T):
    N, M = map(int, input().split())
    Ci = list(map(int, input().split()))

    queue = [[-1, -1]] * N
    result = []
    oven_door = 0
    i = 0

    while True:
        if queue[oven_door][0] == 0:
            result.append(queue[oven_door])
            queue[oven_door] = [-1, -1]

        if queue[oven_door][0] == -1:
            if i < len(Ci):
                queue[oven_door] = [Ci[i], i]
                i += 1

        oven_door = (oven_door + 1) % len(queue)

        queue[oven_door][0] //= 2

        if all_done(queue):
            break

    print(f"#{t + 1} {result[-1][1] + 1}")