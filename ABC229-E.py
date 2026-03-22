def find(x):
    while parent[x] != x:
        parent[x] = parent[parent[x]]
        x = parent[x]
    return x

def union(a, b):
    ra, rb = find(a), find(b)
    if ra == rb: 
        return
    if size[ra] < size[rb]:
        ra, rb = rb, ra
    parent[rb] = ra
    size[ra] += size[rb]
n,m=map(int,input().split())
nodes=[[] for _ in range(n+1)]
for i in range(m):
    a,b=map(int,input().split())
    nodes[a].append(b)
    nodes[b].append(a)
parent=[]
size=[]
for i in range(n+1):
    parent.append(i)
    size.append(1)
count=0
points=0
ans=[0]
for i in range(n,1,-1):
    points+=1
    for k in nodes[i]:
        if k>=i:
            if find(i)!=find(k):
                union(i,k)
                count+=1
    ans.append(points-count)
ans.reverse()
for i in ans:
    print(i)
