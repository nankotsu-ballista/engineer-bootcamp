from collections import deque
t=int(input())
for _ in range(t):
    n,m,x,y=map(int,input().split())
    nodes=[[] for _ in range(n+1)]
    for i in range(m):
        u,v=map(int,input().split())
        nodes[u].append(v)
        nodes[v].append(u)
    for i in range(n+1):
        nodes[i].sort()
    q=deque()
    q.append((x,[]))
    visited=[False]*(n+1)
    def canreach(points,path):
        QU=deque()
        visitedin=[-1]*(n+1)
        for k in path:
            visitedin[k]=0
        QU.append(y)
        visitedin[y]=1
        #print("QU",QU)
        while QU:
            c=QU.pop()
            for i in nodes[c]:
                if visitedin[i]==-1:
                    QU.append(i)
                    visitedin[i]=1
        ans=[]
        for i in points:
            if visitedin[i]==1:
                ans.append(i)
            
        #print(visitedin)
        return(ans)
        

    #print("c",c)
    #print(nodes[3])
            
    while q:
        #print(q)
        p,path=q.popleft()
        path.append(p)
        if p==y:
            break
        c=canreach(nodes[p],path)
        #print(c)
        if len(c)>0:
            q.append((min(c),path))
    print(*path)
        
        
        
        
        
    
    