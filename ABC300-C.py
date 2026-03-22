H, W = map(int, input().split())
C = [input() for _ in range(H)]
N = min(H, W)
ans = [0] * N

# 中心 (i,j) を全探索
for i in range(H):
    for j in range(W):
        if C[i][j] != "#":
            continue
        d = 1
        while True:
            ok = True
            for dx, dy in [(-d, -d), (-d, d), (d, -d), (d, d)]:
                ni, nj = i + dx, j + dy
                if 0 <= ni < H and 0 <= nj < W:
                    if C[ni][nj] != "#":
                        ok = False
                        break
                else:
                    ok = False
                    break
            if ok:
                d += 1
            else:
                break
        if d - 1 > 0:
            ans[d - 2] += 1  # サイズ1のバツはd=2のときに検出される

print(" ".join(map(str, ans)))