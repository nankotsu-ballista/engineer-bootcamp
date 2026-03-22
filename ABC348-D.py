from collections import deque
h,w=map(int,input().split())
A=[list(map(str,input().strip())) for _ in range(h)]
n=int(input())
medicines=[[] for _ in range(n+2)]
dx=[1,-1,0,0]
dy=[0,0,1,-1]
medipos=[[0]*w for _ in range(h)]
startpoint=-1
medi=[]
for i in range(h):
    for k in range(w):
        if A[i][k]=="S":
            medipos[i][k]=-1
        if A[i][k]=="T":
            medipos[i][k]=n+1
for i in range(n):
    r,c,e=map(int,input().split())
    if medipos[r-1][c-1]==-1:
        medi.append((r,c,e))
        startpoint=i+1
    else:
        medi.append((r,c,e))
    medipos[r-1][c-1]=i+1

    
for i in range(n):
    visited=[[0]*w for _ in range(h)]
    r,c,e=medi[i]
    q=deque()
    q.append((r-1,c-1,e))
    while q:
        y,x,energy=q.popleft()
        if energy==0:
            continue
        for il in range(4):
            nx=x+dx[il]
            ny=y+dy[il]
            if -1<nx<w and -1<ny<h:
                if visited[ny][nx]==1:
                    continue
                else:
                    if A[ny][nx]=="#":
                        continue
                    else:
                        visited[ny][nx]=1
                        q.append((ny,nx,energy-1))
                        if medipos[ny][nx]!=0:
                            medicines[i+1].append(medipos[ny][nx])
# print(startpoint)
    
# for k in medicines:
#     print(k)
# for k in medipos:
#     print(k)
c=deque()
if startpoint:
    c.append(startpoint)
    visited=[False]*(n+2)
    while c:
        point=c.pop()
        if point == n+1:
            print("Yes")
            exit()
        for a in medicines[point]:
            if visited[a]==True:
                continue
            else:
                visited[a]=True
                c.append(a)
print("No")
    

                         
                
            