H, W = map(int, input().split())
grid = [list(input().strip()) for _ in range(H)]

cookie_positions = []

for i in range(H):
    for j in range(W):
        if grid[i][j] == "#":
            cookie_positions.append((i, j))

# クッキーがあった長方形の上下左右の端を求める
min_i = min(i for i, _ in cookie_positions)
max_i = max(i for i, _ in cookie_positions)
min_j = min(j for _, j in cookie_positions)
max_j = max(j for _, j in cookie_positions)

# その範囲内で '.' の場所が答え
for i in range(min_i, max_i + 1):
    for j in range(min_j, max_j + 1):
        if grid[i][j] == ".":
            print(i + 1, j + 1)  # 1-indexedで出力
            exit()
