from collections import deque
import heapq
n,m=map(int,input().split())
H=list(map(int,input().split()))
H=[0]+H
nodes=[[] for _ in range(n+1)]
for i in range(m):
    u,v=map(int,input().split())
    nodes[u].append(v)
    nodes[v].append(u)
hq=[]
heapq.heappush(hq,(0,1))
cost=[10**18]*(n+1)
cost[1]=0
#print(nodes)
while hq:
    d,idx=heapq.heappop(hq)
    for i in nodes[idx]:
        if cost[i]>cost[idx]+(max(0,H[i]-H[idx])):
            cost[i]=cost[idx]+(max(0,H[i]-H[idx]))
            heapq.heappush(hq,(cost[idx]+(max(0,H[i]-H[idx])),i))
ans=0
#print(cost)
for i in range(2,n+1):
    ans=max(ans,H[1]-H[i]-cost[i])
    #print(H[1]-H[i]-cost[i])
print(ans)