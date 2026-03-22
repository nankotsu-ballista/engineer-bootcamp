from collections import deque
n,m=map(int,input().split())
nodes=[[] for _ in range(n+1)]
for i in range(m):
    a,b=map(int,input().split())
    nodes[a].append(b)
    nodes[b].append(a)
#print(nodes)
q=int(input())
for i in range(q):
    s=set()
    x,k=map(int,input().split())
    s.add(x)
    que=deque()
    que.append((x,0))
    while que:
        
        nxt,t=que.popleft()
        if t==k:
            continue
        for nd in nodes[nxt]:
            if nd not in s:
                que.append((nd,t+1))
                s.add(nd)
    ans=0
    #print(s)
    for t in s:
        ans+=t
    print(ans)