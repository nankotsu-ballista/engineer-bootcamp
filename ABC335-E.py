import heapq
n,m=map(int,input().split())
A=[0]+list(map(int,input().split()))
nodes=[[]for _ in range(n+1)]
for i in range(m):
    u,v=map(int,input().split())
    if A[u]>A[n] or A[v]>A[n]:
        continue
    if A[v]>=A[u]:
        nodes[u].append(v)
    if A[u]>=A[v]:
        nodes[v].append(u)
ways=[-1]*(n+1)
#print(nodes)
hq=[]
heapq.heappush(hq,(A[1],-1,1))
ways[1]=1
ans=0
visited=[False]*(n+1)
while hq:
    #print(hq)
    high,way,idx=heapq.heappop(hq)
    if visited[idx]==True:
        continue
    visited[idx]=True
    if idx==n:
        ans=-way
        break
    way=(-way)
    for i in nodes[idx]:
        if visited[i]==True:
            continue
        if ways[i]<way+1:
            if A[i]==A[idx]:
                heapq.heappush(hq,(A[i],-way,i))
                ways[i]=way
            else:    
                heapq.heappush(hq,(A[i],-way-1,i))
                ways[i]=way+1
print(ans)
    
