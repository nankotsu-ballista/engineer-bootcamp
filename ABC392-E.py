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
n,m=map(int,input().split())
parent=[]
size=[]
for i in range(n+1):
    parent.append(i)
    size.append(1)
afford=deque()
renketu=n
for t in range(m):
    a,b=map(int,input().split())
    if find(a)==find(b):
        afford.append((t+1,a,b))
    else:
        renketu-=1
    union(a,b)
#print(afford)
#print(renketu)
# if len(afford)<renketu+1:
#     print("No")
#     exit()
oyaset=set()
for i in range(1,n+1):
    oyaset.add(find(i))
#print(oyaset)
print(renketu-1)
while afford:
    if renketu==1:
        exit()
    t,a,b=afford.popleft()
    for k in oyaset:
        if find(a)==find(k):
            continue
        else:
            union(a,k)
            print(t,a,k)
            oyaset.discard(k)
            break

            
        
    
