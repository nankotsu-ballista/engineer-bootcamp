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
parent=[]
size=[]
group=0
for i in range(n+1):
    parent.append(i)
    size.append(1)
for i in range(m):
    a,b,c,d=map(str,input().split())
    a=int(a)
    c=int(c)
    if find(a)==find(c):
        group+=1
    union(a,c)
#print(parent)
s=set()
for i in range(1,n+1):
    a=find(i)
    s.add(a)
print(group,len(s)-group)
    