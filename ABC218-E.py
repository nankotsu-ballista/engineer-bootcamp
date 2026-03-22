import heapq
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

hq=[]
n,m=map(int,input().split())
parent=[]
size=[]
for i in range(n+1):
    parent.append(i)
    size.append(1)
csum=0
hunosu=0
for i in range(m):
    a,b,c=map(int,input().split())
    heapq.heappush(hq,(c,a,b))
    csum+=c
    if c<0:
        hunosu+=c
count=0
ans=0
usedhunosu=0
# print(hunosu)
# print(usedhunosu)
while hq and count!=n-1:
    c,a,b=heapq.heappop(hq)
    if find(a)!=find(b):
        union(a,b)
        count+=1
        ans+=c
        if c<0:
            usedhunosu+=c
a=(hunosu-usedhunosu)
print(csum-ans-a)
        
    
    