from itertools import combinations
n,m,kk=map(int,input().split())
nodes=[]
for i in range(m):
    u,v,w=map(int,input().split())
    nodes.append((u-1,v-1,w))
t=[i for i in range(m)]
#print(nodes)
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
ans=10**18
for comb in combinations(t,n-1):
    parent=[i for i in range(n)]
    size=[1]*n
    sum=0
    for k in comb:
        tmpu,tmpv,cost=nodes[k]
        union(tmpu,tmpv)
        sum+=cost
    check=True
    for k in range(n):
        if find(0)!=find(k):
            check=False
            break
    if check==True:
        ans=min(sum%kk,ans)
    # print(comb)
    # print(check)
    # print(sum)
print(ans)





