h,w,k=map(int,input().split())
grid=[input() for _ in range(h)]
visited=[[False]*w for _ in range(h)]
ans=0
def dfs (i,j,count):
    global ans
    if count==k:
        ans += 1
        return
    visited[i][j]=True
    for di, dj in [(1,0),(0,1),(-1,0),(0,-1)]:
        ni,nj = i +di,j+dj
        if ni<h and 0<=ni and 0<=nj and nj<w and grid[ni][nj]=="." and not visited[ni][nj]:
            dfs(ni,nj,count+1)
    visited[i][j]=False
    
for i in range(h):
    for j in range(w):
        if grid[i][j]==".":
            dfs(i,j,0)
print(ans)