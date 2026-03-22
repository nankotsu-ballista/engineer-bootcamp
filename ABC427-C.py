import itertools
l = []
nodes=[]
n,m=map(int,input().split())
for i in range(n):
    l.append(i+1)
for i in range(m):
        u,v=map(int,input().split())
        nodes.append((u,v))
#print(nodes)
ans=10**10
for i in range(n):
    for vv in itertools.combinations(l, i):
        vv=set(vv)
        #print(vv)
        count=0
        for k in range(m):
            ur,vr=nodes[k]
            if (ur in vv and vr in vv) or (ur not in vv and vr not in vv):
                count+=1
        ans=min(ans,count)
        #print(count)
print(ans)
    