from collections import deque
n,m=map(int,input().split())
s = [input().strip() for _ in range(n)]
q=deque()
q.append((1,1,4))
dx=[0,0,1,-1]
dy=[1,-1,0,0]
visited = [[[0]*5 for _ in range(m)] for _ in range(n)]
visited[1][1][4]=1
while q:
    x,y,direct=q.popleft()
    if direct==4:
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0<=nx<n and 0<=ny<m and s[nx][ny]==".":
                if visited[nx][ny][i]==0:
                    visited[nx][ny][i]=1
                    q.append((nx,ny,i))
    else:
        nx = x + dx[direct]
        ny = y + dy[direct]
        if 0<=nx<n and 0<=ny<m and s[nx][ny]==".":
                if visited[nx][ny][direct]==0:
                    visited[nx][ny][direct]=1
                    q.append((nx,ny,direct))
        else:
            if visited[x][y][4] == 0:
                visited[x][y][4] = 1
                q.append((x,y,4))
res = 0
visitor=[[0]*m for _ in range(n)] 
for i in range(n):
    for j in range(m):
        for k in range(5):
            if visited[i][j][k]==1:
                visitor[i][j]=1
#print(visitor)
ans=0
for i in range(n):
    for j in range(m):
        if visitor[i][j]==1:
            ans+=1
print(ans)
                
                
                    
            