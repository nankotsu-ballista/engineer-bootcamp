from collections import deque
h,w=map(int,input().split())
grid=[list(map(str,input().strip())) for _ in range(h)]
Y1,X1,Y2,X2=map(int,input().split())
q=deque()
q.appendleft((Y1-1,X1-1))
#print(q)
INF=10**18
dy=[1,-1,0,0]
dx=[0,0,1,-1]
cost=[[INF]*w for _ in range(h)]
cost[Y1-1][X1-1]=0
while q:
    i,k=q.popleft()
    if (i+1)==Y2 and (k+1)==X2:
        print(cost[i][k])
        #print(cost)
        exit()
    for c in range(4):
        ny=i+dy[c]
        nx=k+dx[c]
        if not (0<=nx<w and 0<=ny<h):
            continue
        if grid[ny][nx]==".":
            if cost[i][k]<cost[ny][nx]:
                cost[ny][nx]=cost[i][k]
                q.appendleft((ny,nx))
        else:
            for cc in range(2):
                ny=i+dy[c]*(cc+1)
                nx=k+dx[c]*(cc+1)
                #print(ny,nx)
                if not (0<=nx<w and 0<=ny<h):
                    continue
                if cost[i][k]+1<cost[ny][nx]:
                    cost[ny][nx]=cost[i][k]+1
                    q.append((ny,nx))
print(cost)
            
            
        
        
    
    