import heapq
n,m=map(int,input().split())
nodes=[[] for _ in range(n+1)]
for i in range(m):
    a,b,c=map(int,input().split())
    nodes[a].append((i,b,c))
    nodes[b].append((i,a,c))
hq=[]
heapq.heappush(hq,(0,1))
costs=[10**18]*(n+1)
hosyu=[-1]*(n+1)
costs[1]=0
#print(nodes[2])
visited=[False]*(n+1)
count=0
while hq:
    if count==n-1:
        break
    cost,idx=heapq.heappop(hq)
    if visited[idx]==True:
        continue
    visited[idx]=True
    count+=1
    for i,nd,c in nodes[idx]:
        if costs[nd]>cost+c:
            costs[nd]=cost+c
            heapq.heappush(hq,(cost+c,nd))
            hosyu[nd]=i
#print(hosyu)
ans=[]
for i in hosyu:
    if i == -1:
        continue
    else:
        ans.append(i+1)
print(*ans)
    

    