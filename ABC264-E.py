from collections import deque
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
parent=[]
size=[]
n,m,e=map(int,input().split())
for i in range(n+m+1):
    parent.append(i)
    size.append(1)
items=[]
for i in range(e):
    u,v=map(int,input().split())
    items.append((u,v))
q=int(input())
setsudanitems=[]
setsudan=set()
for i in range(q):
    x=int(input())
    setsudanitems.append(x)
    setsudan.add(x)
denki=[False]*(n+1)+[True]*(m)
#print(denki)
ans=0
for i in range(e):
    if i+1 in setsudan:
        continue
    u,v=items[i]
    if denki[find(u)] or denki[find(v)]:
        if denki[find(u)]==False:
            ans+=size[find(u)]
        if denki[find(v)]==False:
            ans+=size[find(v)]
        denki[find(u)]=True
        denki[find(v)]=True
    union(u,v)
# print(ans)
# print(denki)
# print(size)
# print(parent)
newitems=[]
setsudanitems.reverse()
for i in setsudanitems:
    newitems.append(items[i-1])
#print(newitems)
anss=[ans]
for i in range(q-1):
    u,v=newitems[i]
    if denki[find(u)] or denki[find(v)]:
        if denki[find(u)]==False:
            ans+=size[find(u)]
        if denki[find(v)]==False:
            ans+=size[find(v)]
        denki[find(u)]=True
        denki[find(v)]=True
    union(u,v)
    anss.append(ans)
anss.reverse()
#print(anss)
for i in anss:
    print(i)







