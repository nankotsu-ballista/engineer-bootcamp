from collections import deque
h,w=map(int,input().split())
grid=[list(map(str,input().strip())) for _ in range(h)]
for i in range(h):
    for k in range(w):
        if grid[i][k]=="S":
            start=(i,k)
        if grid[i][k]=="G":
            goal=(i,k)
#print(start)
dist=[[-1]*w for _ in range(h)]
#print(dist)
i,j=start
dist[i][j]=1
q=deque()
q.append((i,j,0))
gi,gj=goal
check=False
while q:
    i,j,v=q.popleft()
    if i == gi and j ==gj:
        check=True
        break
    
    if v==0:
        if j+1<w and dist[i][j+1]==-1 and grid[i][j+1]!="#":
            q.append((i,j+1,1))
            dist[i][j+1]=dist[i][j]+1
        if j-1>=0 and dist[i][j-1]==-1 and grid[i][j-1]!="#":
            q.append((i,j-1,1))
            dist[i][j-1]=dist[i][j]+1
    elif v==1:
        if i+1<h and dist[i+1][j]==-1 and grid[i+1][j]!="#":
            q.append((i+1,j,0))
            dist[i+1][j]=dist[i][j]+1
        if i-1>=0 and dist[i-1][j]==-1 and grid[i-1][j]!="#":
            q.append((i-1,j,0))
            dist[i-1][j]=dist[i][j]+1
    #print(q)
tatec=dist[gi][gj]
dist=[[-1]*w for _ in range(h)]
#print(dist)
i,j=start
q=deque()
q.append((i,j,1))
dist[i][j]=1
gi,gj=goal
check=False
while q:
    i,j,v=q.popleft()
    if i == gi and j ==gj:
        check=True
        break
    
    if v==0:
        if j+1<w and dist[i][j+1]==-1 and grid[i][j+1]!="#":
            q.append((i,j+1,1))
            dist[i][j+1]=dist[i][j]+1
        if j-1>=0 and dist[i][j-1]==-1 and grid[i][j-1]!="#":
            q.append((i,j-1,1))
            dist[i][j-1]=dist[i][j]+1
    elif v==1:
        if i+1<h and dist[i+1][j]==-1 and grid[i+1][j]!="#":
            q.append((i+1,j,0))
            dist[i+1][j]=dist[i][j]+1
        if i-1>=0 and dist[i-1][j]==-1 and grid[i-1][j]!="#":
            q.append((i-1,j,0))
            dist[i-1][j]=dist[i][j]+1
    #print(q)
#print(*dist)
yokoc=dist[gi][gj]
if yokoc==-1:
    yokoc=10**18
if tatec==-1:
    tatec=10**18
if tatec ==10**18 and yokoc ==10**18:
    print(-1)
else:
    print(min(yokoc,tatec)-1)



