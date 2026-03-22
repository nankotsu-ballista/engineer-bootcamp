import sys
sys.setrecursionlimit(200001)
from collections import deque
n=int(input())
nodes=[[] for _ in range(n+1)]
q=deque()
for i in range(n-1):
    u,v=map(int,input().split())
    nodes[u].append(v)
    nodes[v].append(u)
visited=[False]*(n+1)
q.append(1)
costs=[0]*(n+1)
kyoris=[0]*(n+1)
def dfs(a,kyori):
    cost=1
    for i in nodes[a]:
        if visited[i]==False:
            visited[i]=True
            cost+=dfs(i,kyori+1)
    costs[a]=cost
    kyoris[a]=kyori
    return cost
visited[1]=True
dfs(1,0)
# print(costs)
# print(kyoris)
visited=[False]*(n+1)
visited[1]=True
anss=[-1]*(n+1)
ans=sum(kyoris)
q=deque()
q.append((1,ans))
while q:
    idx,ans=q.popleft()
    anss[idx]=ans
    for i in nodes[idx]:
        if visited[i]==False:
            visited[i]=True
            q.append((i,ans+n-2*(costs[i])))
for i in range(1,n+1):
    print(anss[i])
         