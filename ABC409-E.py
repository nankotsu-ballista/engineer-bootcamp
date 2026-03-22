from collections import deque
n=int(input())
x=list(map(int,input().split()))
x=[0]+x
costs={}
nodes=[[] for _ in range(n+1)]
for _ in range(n-1):
    u,v,w=map(int,input().split())
    costs[(u,v)] = w
    costs[(v,u)] = w
    nodes[u].append(v)
    nodes[v].append(u)
q=deque()
q.append((-1,1,0))
#print(costs.get((1,2), 0))
ans=0
#print(q)
while q:
    root,node,check=q.pop()
    if root==-1 and check==1:
        break
    if check==0:
        q.append((root,node,1))
        for k in nodes[node]:
            if k!=root:
                q.append((node,k,0))
    else:
        ans+=abs(x[node])*costs.get((root,node), 0)
        x[root]+=x[node]
        x[node]=0
    #print(q)
# print(x)
print(ans)
# print(nodes)
        
    
    