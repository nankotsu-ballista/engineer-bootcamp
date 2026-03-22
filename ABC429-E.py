from collections import deque
n,m=map(int,input().split())
nodes=[[]for _ in range(n+1)]
se=[set() for _ in range(n+1)]
#print(se)
for _ in range(m):
    u,v=map(int,input().split())
    nodes[u].append(v)
    nodes[v].append(u)
S=list(input())
q=deque()
visited=[0]*(n+1)
#print(visited)
for i in range(n):
    if S[i]=="S":
        q.append((i+1,i+1,0))
#print(q)
costs=[[] for _ in range(n+1)]
while q:
    #print(q)
    point,root,cost=q.popleft()
    for i in nodes[point]:
        if root not in se[i]:
            if len(se[i])>=2:
                continue
            else:
                se[i].add(root)
                costs[i].append(cost+1)
                q.append((i,root,cost+1))
# print(se)
# print(costs)
for i in range(n):
    if S[i] == "D":
        print(costs[i+1][0]+costs[i+1][1])
                
            