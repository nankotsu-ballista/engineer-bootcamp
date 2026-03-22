from collections import deque
n=int(input())
X=[0]+list(map(int,input().split()))
C=[0]+list(map(int,input().split()))
visited=[False]*(n+1)
nyuujisu=[0]*(n+1)
for i in range(1,n+1):
    nyuujisu[X[i]]+=1
#print(nyuujisu)
q=deque()
for i in range(1,n+1):
    if nyuujisu[i]==0:
        q.append(i)
while q:
    nxt=q.popleft()
    nyuujisu[X[nxt]]-=1
    if nyuujisu[X[nxt]]==0:
        q.append(X[nxt])
#print(nyuujisu)
ans=0
for i in range(1,n+1):
    tmp=[]
    if nyuujisu[i]==0:
        continue
    q=deque()
    q.append(i)
    nyuujisu[i]-=1
    tmp.append(i)
    while q:
        nx=q.popleft()
        if nyuujisu[X[nx]]==1:
            nyuujisu[X[nx]]-=1
            q.append(X[nx])
            tmp.append(X[nx])
    minans=10**18
    #print(tmp)
    for c in tmp:
        minans=min(minans,C[c])
    ans+=minans
print(ans)
