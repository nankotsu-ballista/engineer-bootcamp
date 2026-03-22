import sys
sys.setrecursionlimit(10**6)

n, k = map(int, input().split())
r = list(map(int, input().split()))

seq = []

def dfs(lv, current):
    if lv == n:
        if sum(current) % k == 0:
            print(*current)
        return
    for i in range(1, r[lv] + 1):
        dfs(lv + 1, current + [i])

dfs(0, [])
