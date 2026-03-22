import sys
sys.setrecursionlimit(10**6)
dx =[1,0,-1,0,1,1,-1,-1]
dy =[0,1,0,-1,1,-1,1,-1]

h, w = map(int, input().split())
s = [list(input()) for _ in range(h)]
used = [[False] * w for _ in range(h)]

def dfs(x, y):
    stack = [(x, y)]
    used[x][y] = True
    while stack:
        cx, cy = stack.pop()
        for d in range(8):
            nx = cx + dx[d]
            ny = cy + dy[d]
            if 0 <= nx < h and 0 <= ny < w and s[nx][ny] == "#" and not used[nx][ny]:
                used[nx][ny] = True
                stack.append((nx, ny))

ans = 0
for i in range(h):
    for j in range(w):
        if s[i][j] == "#" and not used[i][j]:
            dfs(i, j)
            ans += 1

print(ans)