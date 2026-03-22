import heapq,bisect
n,m,k=map(int,input().split())
roads=[-1]
for i in range(m):
    a,b,c=map(int,input().split())
    roads.append((a,b,c))

E=list(map(int,input().split()))
idxs=[[] for _ in range(m+1)]
costs=[10**18]*(n+1)
costs[1]=0
for i in range(k):
    a,b,c=roads[E[i]]
    costs[b]=min(costs[b],costs[a]+c)
if costs[-1]==10**18:
    print(-1)
else:
    print(costs[-1])