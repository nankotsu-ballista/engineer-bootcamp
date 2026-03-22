from collections import defaultdict
n,m=map(int,input().split())
count=0
edge= defaultdict(int)
node=[[] for _ in range(n+1)]
for i in range(m):
    u,v=map(int,input().split())
    if u == v:
        count+=1
    else:
        a,b=sorted((u,v))
        edge[(a,b)] +=1
#print(edge)
for pair in edge:
    if edge[pair] >=2:
        count += edge[pair]-1 
print(count)