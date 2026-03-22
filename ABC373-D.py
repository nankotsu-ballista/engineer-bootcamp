from collections import deque
n,m=map(int,input().split())
dist=[0]*(n+1)
check=[False]*(n+1)
omomi=[[] for _ in range(n+1)]
for i in range(m):
    u,v,w=map(int,input().split())
    omomi[u].append((v,w))
    omomi[v].append((u,-w))
q=deque()
#print(omomi)
for j in range(1,n+1):
    if check[j]==False:
        q.append(j)
        check[j]=True
        while q:
            c=q.popleft()
            for i in range(len(omomi[c])):
                idx,cost=omomi[c][i]
                if check[idx]==False:
                    q.append(idx)
                    dist[idx]=dist[c]+cost
                    check[idx]=True
a=dist[1:]
print(' '.join(map(str, a)))    
        
        
    
    
            
    