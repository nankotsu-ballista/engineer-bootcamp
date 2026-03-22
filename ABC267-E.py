from collections import deque
n,m=map(int,input().split())
A=[0]+list(map(int,input().split()))
nodes=[[] for _ in range(n+1)]
for i in range(m):
    u,v=map(int,input().split())
    nodes[u].append(v)
    nodes[v].append(u)
costs=[0]*(n+1)
for i in range(1,n+1):
    for k in nodes[i]:
        costs[i]+=A[k]
#print(costs)
right=max(costs)
left=0
        
while left<right:
    mid=(left+right)//2
    count=0
    hq=deque()
    tmpcost=[]
    for i in costs:
        tmpcost.append(i)
    visited=[False]*(n+1)
    for i in range(1,n+1):
        if tmpcost[i]<=mid:
            hq.append((tmpcost[i],i))
    while hq:
        costnt,nxt=hq.popleft()
        if visited[nxt]==False:
            visited[nxt]=True
            count+=1
        else:
            continue
        tmpcost[nxt]=0
        for nt in nodes[nxt]:
            tmpcost[nt]-=A[nxt]
            if tmpcost[nt]<=mid and visited[nt]==False:
                hq.append((tmpcost[nt],nt))
                
    #print(visited)
    if count!=n:
        left=mid+1
    else:
        right=mid
print(left)
