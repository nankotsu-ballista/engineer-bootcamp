from collections import deque
n,m=map(int,input().split())
nodes=[[] for _ in range(n+1)]
for i in range(m):
    a,b,w=map(int,input().split())
    nodes[a].append((b,w))
#print(nodes)
cost=[[0]*1024 for _ in range(n+1)]
#print(cost)
q=deque()
q.append((1,0))
# print(nodes)
# print(cost)
while q:
    point,cos=q.popleft()
    for node,ww in nodes[point]:
        cosp=ww^cos
        if cost[node][cosp]==0:
            cost[node][cosp]=1
            q.append((node,cosp))
#print(cost[n])
ans=-1
for i in range(len(cost[n])):
    if cost[n][i] ==1:
        ans=i
        break
print(ans)
    