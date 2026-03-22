import sys
sys.setrecursionlimit(10**6+20)

n,m=map(int,input().split())
nodes=[[]for _ in range(n+1)]
for i in range(m):
    u,v=map(int,input().split())
    nodes[u].append(v)
    nodes[v].append(u)
visited=[False]*(n+1)
limit=10**6
path=[]
ans=0
def dfs(c):
    global ans
    if ans==limit:
        return
    visited[c]=True
    ans+=1
    for i in nodes[c]:
        if visited[i]==False:
            dfs(i)
    visited[c]=False
dfs(1)
print(ans)