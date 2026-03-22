from collections import deque
n,m=map(int,input().split())
nodes=[[]for _ in range(n+1)]
sakujo=set()
maxnum=-1
for i in range(m):
    u,v,w=map(int,input().split())
    nodes[u].append((i,v,w))
    nodes[v].append((i,u,w))
    maxnum=max(maxnum,w)

length=len(bin(maxnum))-2
#print(length)
ans=[]
for i in range(length-1,-1,-1):
    #print(i)
    tmpsakujo=set()
    visited=set()
    q=deque()
    q.append(1)
    visited.add(1)
    reachable=False
    while q:
        #print(q)
        idx=q.popleft()
        if idx == n:
            ans.append(0)
            reachable=True
        for idd,j,cost in nodes[idx]:
            if idd in sakujo:
                continue
            if cost & (1<<i):
                tmpsakujo.add(idd)
            else:
                if j not in visited:
                    visited.add(j)
                    q.append(j)
    if reachable==False:
        ans.append(1)
    else:
        for kk in tmpsakujo:
            sakujo.add(kk)
trueans=0
ans.reverse()
for i in range(len(ans)):
    trueans+=(2**i)*ans[i]
print(trueans)
            
