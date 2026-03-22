from collections import deque
n,m=map(int,input().split())
node=[[] for _ in range(n)]
for i in range(m):
    a,b=map(int,input().split())
    node[a-1].append(b-1)
    node[b-1].append(a-1)
visited=[False]*n
k=0
for i in range(n):
    if visited[i]:
        continue
    k+=1
    q=deque()
    q.append(i)
    visited[i]=True
    while q:
        current= q.popleft()
        for neighbor in node[current]:
            if not visited[neighbor]:
                visited[neighbor] =True
                q.append(neighbor)
print(m-(n-k))
    
    



    