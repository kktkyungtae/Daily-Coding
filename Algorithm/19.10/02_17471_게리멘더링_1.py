import itertools, collections

def make_sector(sector):
    rtn = list(range(1, N+1))
    for n in sector:
        rtn.remove(n)
    return tuple(rtn)

def sector_validation(sector, check):
    q = collections.deque()
    cnt = 1
    visited[sector[0]] = True
    q.append(sector[0])

    while q:
        v = q.popleft()
        for nv in adj[v]:
            if nv in sector and not visited[nv]:
                visited[nv] = True
                cnt += 1
                q.append(nv)
    if cnt == check:
        return True
    else:
        return False

def sector_population(sector):
    rtn = 0
    for n in sector:
        rtn += population[n]
    return rtn

N = int(input())
population = [0]+list(map(int, input().split()))
adj = [0]+[list(map(int, input().split()[1:])) for _ in range(N)]
min_diff = 999999999

for n in range(1, (N//2)+1):
    for sector1 in itertools.combinations(range(1, N+1), n):
        sector2 = make_sector(sector1)
        visited = [False]*(N+1)
        if sector_validation(sector1, n) and sector_validation(sector2, N-n):
            min_diff = min(min_diff, abs(sector_population(sector1)-sector_population(sector2)))

if min_diff != 999999999:
    print(min_diff)
else:
    print(-1)