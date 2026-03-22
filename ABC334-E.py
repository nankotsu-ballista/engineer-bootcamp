from collections import deque
import math
h,w=map(int,input().split())
grid=[list(map(str,input().strip())) for _ in range(h)]
visited=[[-1]*w for _ in range(h)]
#print(grid)
dx=[0,0,1,-1]
dy=[1,-1,0,0]
islandid=0
for i in range(h):
    for k in range(w):
        if visited[i][k]==-1 and grid[i][k]=="#":
            islandid+=1
            q=deque()
            q.append((i,k))
            #print(q)
            while q:
                y,x=q.popleft()
                visited[y][x]=islandid
                for d in range(4):
                    nx=x+dx[d]
                    ny=y+dy[d]
                    if -1<nx<w and -1<ny<h and grid[ny][nx]=="#" and visited[ny][nx] == -1:
                        q.append((ny,nx))
                        visited[ny][nx]=islandid
            
#print(visited)
ans=0
sum=0
for i in range(h):
    for k in range(w):
        if grid[i][k]==".":
            s=set()
            check=False
            for d in range(4):
                nx=k+dx[d]
                ny=i+dy[d]
                
                if -1<nx<w and -1<ny<h :
                    s.add(visited[ny][nx])
                    if visited[ny][nx]!=-1:
                        check=True
            s.discard(-1)
            #print(s)
            if len(s)>1:
                ans+=(islandid+1-len(s))
                #print(i,k,(islandid+1-len(s)))
            else:
                ans+=islandid
                #print(i,k,(islandid))
            if check==False:
                ans+=1
            sum+=1
                
                
        
                        
                        
                        
                
MOD = 998244353
ans %= MOD
den = sum % MOD  # 赤マス数（分母）
ans = ans * pow(den, MOD - 2, MOD) % MOD
print(ans)
    