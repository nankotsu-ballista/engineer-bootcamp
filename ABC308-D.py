import sys
sys.setrecursionlimit(10**6)

H, W = map(int,(input().split()))
grid = [list(input()) for _ in range(H)]
visited = [[0] * W for _ in range(H)]

def dfs(i, j, s):
    if i < 0 or i >= H or j < 0 or j >= W:
        return False
    if visited[i][j] == 1:
        return False
    if grid[i][j] != s:
        return False

    visited[i][j] = 1
    if i == H - 1 and j == W - 1:
        return True

    S = "snuke"
    idx = S.find(s)
    next_char = S[(idx + 1) % 5]

    return (
        dfs(i + 1, j, next_char) or
        dfs(i - 1, j, next_char) or
        dfs(i, j + 1, next_char) or
        dfs(i, j - 1, next_char)
    )

if dfs(0, 0, "s"):
    print("Yes")
else:
    print("No")