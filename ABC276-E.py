from collections import deque
h,w=map(int,input().split())
C=[list(map(str,input().strip())) for _ in range(h)]
visited=[[False]*w for _ in range(h)]
for i in range(h):
    for k in range(w):
        if C[i][k]=="S":
            #print(i,k)
            si=i
            sk=k
di=[0,0,1,-1]
dk=[1,-1,0,0]
q=deque()
ans=False
for dd in range(4):
    ni=si+di[dd]
    nk=sk+dk[dd]
    visited=[[False]*w for _ in range(h)]
    q=deque()
    if -1<ni<h and -1<nk<w and C[ni][nk]==".":
        q.append((ni,nk,1))
        visited[ni][nk]=True
    #print(dd)
    while q:
        #print(q)
        ii,kk,time=q.popleft()
        for d in range(4):
            ni=ii+di[d]
            nk=kk+dk[d]
            if ni==si and nk==sk and time>=3:
                print("Yes")
                exit()
            if -1<ni<h and -1<nk<w and C[ni][nk]=="." and visited[ni][nk]==False:
                q.append((ni,nk,time+1))
                visited[ni][nk]=True
print("No")
            
        