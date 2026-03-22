N = int(input())
A = list(map(int, input().split()))
visited = [False] * N

path = []
cur = 0
while not visited[cur]:
    visited[cur] = True
    path.append(cur)
    cur = A[cur] - 1

cycle_start = path.index(cur)
cycle = path[cycle_start:]
print(len(cycle))
print(' '.join(str(x + 1) for x in cycle))
