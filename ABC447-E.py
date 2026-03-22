from collections import deque
def find(x):
    while parent[x] != x:
        parent[x] = parent[parent[x]]
        x = parent[x]
    return x
MOD=998244353
def union(a, b):
    ra, rb = find(a), find(b)
    if ra == rb: 
        return
    if size[ra] < size[rb]:
        ra, rb = rb, ra
    parent[rb] = ra
    size[ra] += size[rb]

    


n,m=map(int,input().split())
items=[]
for i in range(m):
    u,v=map(int,input().split())
    items.append((u,v))
items.reverse()
parent=[]
size=[]
cost=0
renketu=n
for i in range(n+1):
    parent.append(i)
    size.append(1)
#print(items)
nijous=[]
ans=2
for i in range(m):
    nijous.append(ans)
    ans=ans*2%998244353
#print(nijous)
for c in range(m):
    i=items[c][0]
    k=items[c][1]
    if find(i)==find(k):
        continue
    if renketu == 2:
        cost=(cost+nijous[-c-1])%998244353
        continue
    union(i,k)
    renketu-=1
    
print(cost)

