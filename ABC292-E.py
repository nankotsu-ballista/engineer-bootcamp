from collections import deque
n,m=map(int,input().split())
nodes=[[] for _ in range(n+1)]
for i in range(m):
    u,v=map(int,input().split())
    nodes[u].append(v)
cnt=0
q=deque()
for i in range(1,n+1):
    q=deque()
    q.append(i)
    visited=[False]*(n+1)
    visited[i]=True
    while q:
        #print(q)
        idx=q.popleft()
        for j in nodes[idx]:
            if visited[j]==False:
                visited[j]=True
                q.append(j)
                cnt+=1
print(cnt-m)