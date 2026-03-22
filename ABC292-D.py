
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
pointnode=[0]*(2*10**5+1)
for i in range(n+1):
    parent.append(i)
    size.append(1)
for i in range(m):
    u,v=map(int,input().split())
    union(u,v)
    pointnode[u]+=1
#print(parent)
islandpoint=[0]*(2*10**5+1)
islandnode=[0]*(2*10**5+1)
for i in range(1,n+1):
    islandpoint[find(i)]+=1
    islandnode[find(i)]+=pointnode[i]
# print(islandpoint[:10])
# print(islandnode[:10])
for i in range(1,n+1):
    if islandpoint[i] != islandnode[i]:
        print("No")
        exit()
print("Yes")
        
        
        

    