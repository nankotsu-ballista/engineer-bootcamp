from collections import deque
h,w=map(int,input().split())
S=[list(map(str,input().strip())) for _ in range(h)]
visited=[[False]*w for _ in range(h)]
#print(visited)
q=deque()
for i in range(w):
    if S[0][i]==".":
        q.append((0,i))
        visited[0][i]=True
        S[0][i]="#"
    if S[h-1][i]==".":
        q.append((h-1,i))
        visited[h-1][i]=True
        S[h-1][i]="#"
for i in range(1,h-1):
    if S[i][0]==".":
        q.append((i,0))
        visited[i][0]=True
        S[i][0]="#"
    if S[i][w-1]==".":    
        q.append((i,w-1))
        visited[i][w-1]=True
        S[i][w-1]="#"
di=[1,-1,0,0]
dk=[0,0,1,-1]
while q:
    ti,tk=q.popleft()
    for d in range(4):
        ni=ti+di[d]
        nk=tk+dk[d]
        if ni<h and ni>-1 and nk<w and nk>-1 and visited[ni][nk]==False and S[ni][nk]==".":
            q.append((ni,nk))
            visited[ni][nk]=True
            S[ni][nk]="#"
ans=0
# for i in S:
#     print(i)
for i in range(h):
    for k in range(w):
        if visited[i][k]==True or S[i][k]=="#":
            continue
        q=deque()
        q.append((i,k))
        while q:
            ti,tk=q.popleft()
            for d in range(4):
                ni=ti+di[d]
                nk=tk+dk[d]
                if ni<h and ni>-1 and nk<w and nk>-1 and visited[ni][nk]==False and S[ni][nk]==".":
                    q.append((ni,nk))
                    visited[ni][nk]=True
                    S[ni][nk]="#"
        ans+=1
print(ans)
            
            
    
