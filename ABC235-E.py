n,m,q=map(int,input().split())
from collections import defaultdict
s=defaultdict(lambda: defaultdict(int))
se=set()
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
parent=[]
size=[]
for i in range(n+1):
    parent.append(i)
    size.append(1)

hq=[]

for i in range(m):
    a,b,c=map(int,input().split())
    heapq.heappush(hq,(c,a,b,1,-1))
for i in range(q):
    a,b,c=map(int,input().split())
    heapq.heappush(hq,(c,a,b,2,i))
#print(hq)
ans=[""]*q
for i in range(m+q):
    c,a,b,num,idx=heapq.heappop(hq)
    if num==1:
        union(a,b)
    elif num==2:
        if find(a)==find(b):
            ans[idx]="No"
        else:
            ans[idx]="Yes"
for i in ans:
    print(i)
    
