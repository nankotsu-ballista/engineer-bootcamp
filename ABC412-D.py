from itertools import permutations
n,m=map(int,input().split())
nodes=[[] for _ in range(n)]
nodecheck=[[0]*(n+1) for _ in range(n+1)]
for i in range(m):
    a,b=map(int,input().split())
    if a>b:
        a,b=b,a
    nodes[a].append(b)
    nodecheck[a][b]+=1
    nodecheck[b][a]+=1
# print(nodecheck)
# print(nodes)
nodes=[[] for _ in range(n)]
t=[]
for i in range(n):
    t.append(i+1)
#print(t)
ans=10**10
for perm in permutations(t,r=n):
    cost=0
    costcut=0
    for i in range(n):
        if nodecheck[perm[i-1]][perm[i]]==1:
            costcut+=1
        else:
            cost+=1
    #print(cost)
    ans=min(m-costcut+cost,ans)
if n>=6:
    for d in range(3,n-2):
        for perm in permutations(t,r=n):
            perm1=perm[:d]
            perm2=perm[d:]
            cost=0
            costcut=0
            for i in range(d):
                if nodecheck[perm1[i-1]][perm1[i]]==1:
                    costcut+=1
                else:
                    cost+=1
            for i in range(n-d):
                if nodecheck[perm2[i-1]][perm2[i]]==1:
                    costcut+=1
                else:
                    cost+=1
            
            #print(cost)
            ans=min(m-costcut+cost,ans)
print(ans)
            
    
    
        
        