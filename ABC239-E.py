from collections import deque
import heapq
n,q=map(int,input().split())
X=list(map(int,input().split()))
nodes=[[]for _ in range(n+1)]
for i in range(n-1):
    a,b=map(int,input().split())
    nodes[a].append(b)
    nodes[b].append(a)
parent=[-1]*(n+1)
parent[1]=0
qu=deque()
nxtque=[]
qu.append((0,1))
bubunki=[[]for _ in range(n+1)]
for i in range(n):
    bubunki[i+1].append(X[i])
#print(bubunki)
while qu:
    tier,idx=qu.popleft()
    for i in nodes[idx]:
        if parent[i]==-1:
            parent[i]=idx
            qu.append((tier+1,i))
            heapq.heappush(nxtque,(-(tier+1),i))
#print(nxtque)
while nxtque:
    t,idx=heapq.heappop(nxtque)
    #print(t,idx)
    bubunki[parent[idx]]=bubunki[parent[idx]]+bubunki[idx]
    bubunki[parent[idx]].sort()
    bubunki[parent[idx]]=bubunki[parent[idx]][-21:]
#print(bubunki)
# print(parent)
for i in range(q):
    v,k=map(int,input().split())
    print(bubunki[v][-k])