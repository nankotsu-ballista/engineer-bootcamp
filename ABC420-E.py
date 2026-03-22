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
    islandbwcount[ra]=islandbwcount[ra]+islandbwcount[rb]
    islandbwcount[rb]=0
parent=[]
size=[]
n,q=map(int,input().split())
for i in range(n+1):
    parent.append(i)
    size.append(1)
bwchecker=[0]*(n+1)
islandbwcount=[0]*(n+1)
for i in range(q):
    Q=list(map(int,input().split()))
    if Q[0]==1:
        u,v=Q[1],Q[2]
        union(u,v)
    elif Q[0]==2:
        v=Q[1]
        islandid=find(v)
        if bwchecker[v]==0:
            islandbwcount[islandid]+=1
            bwchecker[v]=1
        elif bwchecker[v]==1:
            islandbwcount[islandid]-=1
            bwchecker[v]=0
    elif Q[0]==3:
        v=Q[1]
        if islandbwcount[find(v)]!=0:
            print("Yes")
        else:
            print("No")
#print(parent)
        
        