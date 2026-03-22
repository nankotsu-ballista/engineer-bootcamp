from collections import deque
INF=10**18
n,m=map(int,input().split())
node=[[] for _ in range(n+1)]
pair=[]
for i in range(m):
    a,b=map(int,input().split())
    node[a].append(b)
    pair.append((a,b))
#print(node)
queue=deque()
queue.append(1)
dist = [INF] *(n+1)
dist[1]=0
FF=False
while queue:
    pop=queue.popleft()
    if FF==True:
        if pop == 1:
            break
    FF=True
    for nxt in node[pop]:
        if dist[nxt] == INF:
            dist[nxt]=dist[pop]+1
            queue.append(nxt)
ans=INF
for a,b in pair:
    if b == 1 and dist[a] != INF:
        ans = min(ans,dist[a]+1)
print(ans if ans != INF else -1)
    
            
