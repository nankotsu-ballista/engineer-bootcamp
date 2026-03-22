h, w, k = map(int, input().split())
grid = [input().strip() for _ in range(h)]
ans = 10**18

# 横方向チェック
for i in range(h):
    totalx = 0
    totalten = 0
    yokox = [0] * (w + 1)
    yokoten = [0] * (w + 1)
    for j in range(w):
        if grid[i][j] == "x":
            totalx += 1
        yokox[j + 1] = totalx
        if grid[i][j] == ".":
            totalten += 1
        yokoten[j + 1] = totalten
    for j in range(w - k + 1):
        if yokox[j + k] - yokox[j] == 0:
            ans = min(ans, yokoten[j + k] - yokoten[j])

# 縦方向チェック
for j in range(w):
    totalx = 0
    totalten = 0
    tatex = [0] * (h + 1)
    tateten = [0] * (h + 1)
    for i in range(h):
        if grid[i][j] == "x":
            totalx += 1
        tatex[i + 1] = totalx
        if grid[i][j] == ".":
            totalten += 1
        tateten[i + 1] = totalten
    for i in range(h - k + 1):
        if tatex[i + k] - tatex[i] == 0:
            ans = min(ans, tateten[i + k] - tateten[i])

if ans > k:
    ans = -1
print(ans)
