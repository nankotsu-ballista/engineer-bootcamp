import sys
sys.setrecursionlimit(10**7)
n,m=map(int,input().split())
nodes=[[]for _ in range(n+1)]
nodes2=[[]for _ in range(n+1)]
for i in range(m):
    a,b=map(int,input().split())
    nodes[a].append(b)
    nodes2[b].append(a)
seen=[False]*(n+1)
order = []
def dfs1(v):
    seen[v] = True
    for w in nodes[v]:
        if not seen[w]:
            dfs1(w)
    order.append(v)
for v in range(1,n+1):
    if not seen[v]:
        dfs1(v)
comp=[-1]*(n+1)
sizes=[]
def dfs2(v,cid):
    comp[v]=cid
    count=1
    for w in nodes2[v]:
        if comp[w]==-1:
            count+= dfs2(w,cid)
    return count
cid=0
for v in reversed(order):
    if comp[v]==-1:
        sizes.append(dfs2(v,cid))
        cid+=1
ans=0
for s in sizes:
    ans += s*(s-1)//2
print(ans)