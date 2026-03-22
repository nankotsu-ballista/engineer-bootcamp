n=int(input())
leafs=[0]*(n+1)
nodes=[[] for _ in range(n+1)]
for i in range(n-1):
    u,v=map(int,input().split())
    nodes[u].append(v)
    nodes[v].append(u)
for i in range(n+1):
    leafs[i]=len(nodes[i])-1
# for i in nodes:
#     print(i)
#print(leafs[1:])
sizeyukimax=[]
maxans=0
for i in range(n+1):
    tmpleafs=[]
    for k in nodes[i]:
        tmpleafs.append(leafs[k])
    tmpleafs.sort()
    #print(tmpleafs)
    tmp=0
    L=len(nodes[i])
    for j in range(L):
        tmp=max(tmp,tmpleafs[j]*(L-j)+(L-j))
    #print(tmp+1)
    maxans=max(maxans,tmp+1)    
print(n-maxans)
    


