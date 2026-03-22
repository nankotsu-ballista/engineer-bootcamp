from collections import defaultdict
n,q=map(int,input().split())
nodes=defaultdict(set)
count=[0]*(n+1)
ans=n
#print(count)
for i in range(q):
    Q=list(map(int,input().split()))
    if Q[0]==1:
        u,v=Q[1],Q[2]
        nodes[u].add(v)
        nodes[v].add(u)
        if count[u]==0:
            ans-=1
        if count[v]==0:
            ans-=1
        count[u]+=1
        count[v]+=1
    elif Q[0]==2:
        v=Q[1]
        for k in nodes[v]:
            nodes[k].discard(v)
            count[k]-=1
            if count[k]==0:
                ans+=1
        if len(nodes[v])!=0:
            ans+=1
        nodes[v].clear()
        count[v]=0
    print(ans)
            
        
    