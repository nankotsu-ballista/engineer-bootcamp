from collections import deque
n,m=map(int,input().split())
nodes=[[] for _ in range(n+1)]
for i in range(m):
    u,v=map(int,input().split())
    nodes[u].append(v)
    nodes[v].append(u)
islandlist=[-1]*(n+1)
islandid=0
for i in range(n):
    if islandlist[i]!=-1 :
        continue
    islandid+=1
    q=deque()
    q.append(i)
    islandlist[i]=islandid
    while q:
        k=q.pop()
        for point in nodes[k]:
            if islandlist[point]==-1:
                islandlist[point]=islandid
                q.append(point)
for i in range(1,n+1):
    if islandlist[i]==-1:
        islandid+=1
        islandlist[i]=islandid
s=set()
k=int(input())
for i in range(k):
    x,y=map(int,input().split())
    s.add((islandlist[x],islandlist[y]))
    s.add((islandlist[y],islandlist[x]))
# print(islandlist)
# print(s)
q=int(input())
for i in range(q):
    p,q=map(int,input().split())
    if (islandlist[p],islandlist[q]) in s:
        print("No")
    else:
        print("Yes")