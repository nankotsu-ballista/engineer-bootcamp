from collections import deque
H,W = map(int,input().split())
S = [list(input()) for _ in range(H)]
dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]  # 下、右、上、左
arrows = ['^', '<', 'v', '>']  # 元のマスに戻るための矢印

q = deque()
for i in range(H):
    for j in range(W):
        if S[i][j] == "E":
            q.append([i, j])

while q:
    i,j =q.popleft()
    for d,(di,dj) in enumerate(dirs):
        ni,nj = i+di,j + dj
        if 0 <= ni <H and 0 <= nj < W and S[ni][nj]==".":
            S[ni][nj] = arrows[d]
            q.append((ni,nj))
    
# 出力
for row in S:
    print("".join(row))    