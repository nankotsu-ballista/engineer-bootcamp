from collections import deque
h,w=map(int,input().split())
grid=[list(map(str,input().strip())) for _ in range(h)]
for i in range(h):
    for k in range(w):
        if grid[i][k]=="S":
            starti=i
            startk=k
        if grid[i][k]=="G":
            goali=i
            goalk=k
visitedclose=[[False]*w for _ in range(h)]
visitedopen=[[False]*w for _ in range(h)]
#print(visitedopen)
q=deque()
q.append((starti,startk,0,0))
visitedclose[starti][startk]=True
dx=[0,0,1,-1]
dy=[1,-1,0,0]
cc=0
while q:
    i,k,check,times=q.popleft()
    if i==goali and k == goalk:
        cc=2
        print(times)
        break
    for d in range(4):
        ni=i+dx[d]
        nk=k+dy[d]
        #print(ni)
        if (0 <= ni < h) and (0 <= nk < w):
            if grid[ni][nk]=="S":
                q.append((ni,nk,check,times+1))
                if check==1:
                    visitedopen[ni][nk]=True
            if (check==1 and grid[ni][nk]==".") or (check==1 and grid[ni][nk]=="x") or (grid[ni][nk]=="G"):
                if check == 1 and visitedopen[ni][nk]==False:
                    q.append((ni,nk,1,times+1))
                    visitedopen[ni][nk]=True
            if (check==0 and grid[ni][nk]==".") or (check==0 and grid[ni][nk]=="o") or (grid[ni][nk]=="G"):
                if check == 0 and visitedclose[ni][nk]==False:
                    q.append((ni,nk,0,times+1))
                    visitedclose[ni][nk]=True
            if check==0 and grid[ni][nk]=="?":
                if check == 0 and visitedopen[ni][nk]==False:
                    q.append((ni,nk,1,times+1))
                    visitedopen[ni][nk]=True
            if check==1 and grid[ni][nk]=="?":
                if check == 1 and visitedclose[ni][nk]==False:
                    q.append((ni,nk,0,times+1))
                    visitedclose[ni][nk]=True
    #print(q)
if cc!=2:
    print(-1)
