from collections import deque
n,m=map(int,input().split())
# if n!=m:
#     print(0)
#     exit()
nodes=[[] for _ in range(n+1)]
sakujo=set()
for i in range(m):
    u,v=map(int,input().split())
    nodes[u].append(v)
    nodes[v].append(u)
# for i in range(n+1):
#     if len(nodes[i])==1:
#         sakujo.add(i)
visited = [False]*(n+1)
loopcount=0
for i in range(1,n+1):
    if visited[i]:
        continue
    loopcount+=1
    q=deque()
    q.append(i)
    visited[i]=True
    vcnt=0
    ecnt=0
    while q:
        idx=q.popleft()
        vcnt+=1
        ecnt+=len(nodes[idx])
        for j in nodes[idx]:
            if not visited[j]:
                visited[j]=True
                q.append(j)
    ecnt//=2
    if ecnt != vcnt:
        print(0)
        exit()
    
print(pow(2,loopcount,998244353))
            

    