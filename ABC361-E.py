from collections import deque
import heapq
n=int(input())
costsum=0
nodes=[[]   for _ in range(n+1)]
for i in range(n-1):
    a,b,c=map(int,input().split())
    nodes[a].append((b,c))
    nodes[b].append((a,c))
    costsum+=c
# hq=[]
# heapq.heappush(hq,(1,0))
q=deque()
q.append(1)
visited=[10**18]*(n+1)
maxcost=-1
maxpoint=-1
visited[1]=0
while q:
    point=q.pop()
    for i,cost in nodes[point]:
        if visited[i]>visited[point]+cost:
            visited[i]=min(visited[i],visited[point]+cost)
            q.append(i)
            maxcost=max(maxcost,visited[point]+cost)
for i in range(len(visited)):
    if visited[i]==maxcost:
        maxidx=i
#print(maxidx)

q=deque()
q.append(maxidx)
visited=[10**18]*(n+1)
maxcost=-1
maxpoint=-1
visited[maxidx]=0
#print(nodes)
while q:
    #print(q)
    point=q.pop()
    for i,cost in nodes[point]:
        if visited[i]>visited[point]+cost:
            visited[i]=min(visited[i],visited[point]+cost)
            q.append(i)
            maxcost=max(maxcost,visited[point]+cost)
visited[0]=-1
#print(max(visited))
print(2*costsum-max(visited))

        
    
    