n,m=map(int,input().split())
nodes=[]
for i in range(m):
    u,v=map(int,input().split())
    if u<v:
        nodes.append((u,v))
    else:
        nodes.append((v,u))
minnodes = sorted(nodes, key=lambda x: x[0])
maxnodes = sorted(nodes, key=lambda x: x[1])
#print(maxnodes)
tmp=0
parents=[]
size=[1]*(n+1)
def find(x):
    while parents[x] != x:
        parents[x] = parents[parents[x]]
        x = parents[x]
    return x
comp=0
for i in range(n+1):
    parents.append(i)
#print(parents)
islandcheck=[False]*(n+1)
for i in range(n+1):
    if i ==0:
        continue
    comp+=1
    while tmp<m and maxnodes[tmp][1]<=i:
        u,v=maxnodes[tmp][0],maxnodes[tmp][1]
        parentu,parentv=find(u),find(v)
        if parentu!=parentv:
            if size[parentv] < size[parentu]:
                parentv,parentu=parentu,parentv
            parents[parentu]=parentv
            size[parentv]+=size[parentu]
            comp-= 1
        tmp+=1
    if comp==1:
        islandcheck[i]=True
    #print(i,comp)
#print(islandcheck)
SET=set()
tmp=0
count=0

for i in range(n+1):
    if i==0:
        continue
    if i in SET:
        SET.discard(i)
        count-=1
    if 1==1:
        while tmp<m and minnodes[tmp][0]<=i:
            if minnodes[tmp][1]>i and minnodes[tmp][1] not in SET:
                count+=1
                SET.add(minnodes[tmp][1])
            tmp+=1
    if islandcheck[i]==1:
        print(count)
    else:
        print(-1)
        
        
#print(minnodes)

