from itertools import permutations

def func(order):
    ans = 0
    i = 0
    for inning in innings:
        p, q, r = 0, 0, 0
        out = 0
        while out < 3:
            if inning[order[i]] == 0:
                out += 1
            elif inning[order[i]] == 1:
                ans += p
                p, q, r = q, r, 1
            elif inning[order[i]] == 2:
                ans += p + q
                p, q, r = r, 1, 0
            elif inning[order[i]] == 3:
                ans += p + q + r
                p, q, r = 1, 0, 0
            else:
                ans += p + q + r + 1
                p, q, r = 0, 0, 0
            i = (i+1) % 9
    return ans

n = int(input())
innings = [list(map(int, input().split())) for _ in range(n)]

ans = 0
for permu in permutations(range(1, 9), 8):
    order = list(permu[:3]) + [0] + list(permu[3:])
    ans = max(ans, func(order))

print(ans)

'''
2
4 0 0 0 0 0 0 0 0
4 0 0 0 0 0 0 0 0

2
0 4 4 4 4 4 4 4 4
0 4 4 4 4 4 4 4 4
'''