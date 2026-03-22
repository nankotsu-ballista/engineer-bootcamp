from collections import deque
h,w=map(int,input().split())
grid=[list(map(int,input().split())) for _ in range(h)]
P=list(map(int,input().split()))
for i in range(h):
    for k in range(w):
        grid[i][k]=grid[i][k]-P[i+k]
# for g in grid:
#     print(g)
dp=[[10**18]*w for _ in range(h)]
dp[h-1][w-1]=max(-grid[h-1][w-1],0)
q=deque()
q.append((h-1,w-1))
while q:
    i,k=q.popleft()
    if i>0:
        nv=max(dp[i][k]-grid[i-1][k],0)  # = dp[next] + (P−A) を 0 で下限
        if nv<dp[i-1][k]:                # ★ 小さくなったら更新
            dp[i-1][k]=nv
            q.append((i-1,k))
    if k>0:
        nv=max(dp[i][k]-grid[i][k-1],0)
        if nv<dp[i][k-1]:
            dp[i][k-1]=nv
            q.append((i,k-1))
# for g in dp:
#     print(g)
if dp[0][0]<0:
    print(0)
else:
    print(dp[0][0])
    