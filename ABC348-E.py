import sys
sys.setrecursionlimit(200001)
from collections import deque
n=int(input())
nodes=[[] for _ in range(n+1)]
for i in range(n-1):
    u,v=map(int,input().split())
    nodes[u].append(v)
    nodes[v].append(u)

C=list(map(int,input().split()))
C=[0]+C
visited=[False]*(n+1)
weights=[0]*(n+1)
kyoris=[0]*(n+1)
def dfs(a,kyori):
    weight=C[a]
    for i in nodes[a]:
        if visited[i]==False:
            visited[i]=True
            weight+=dfs(i,kyori+1)
    weights[a]=weight
    kyoris[a]=kyori
    return weight
visited[1]=True
dfs(1,0)
# print(kyoris)
# print(weights)
ans=0
for i in range(1,n+1):
    ans+=kyoris[i]*C[i]
#print(ans)
q=deque()
q.append((1,ans))
anss=[0]*(n+1)
anss[1]=ans
visited=[False]*(n+1)
visited[1]=True
sumC=sum(C)
while q:
    idx,ans=q.popleft()
    anss[idx]=ans
    for i in nodes[idx]:
        if visited[i]==False:
            visited[i]=True
            q.append((i,ans+sumC-2*weights[i]))
print(min(anss[1:]))



