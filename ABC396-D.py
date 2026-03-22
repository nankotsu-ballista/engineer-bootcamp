N,M= map(int, input().split())
G = [[] * N for i in range(N)] 
for i in range(M):
    u,v,w=map(int, input().split())
    u-=1
    v-=1
    G[u].append((v,w))
    G[v].append((u,w))
visited=[False]*N
ans = 1<<60
def dfs(top,xor):
    global ans
    visited[top]=True
    if top==N-1:
        ans=min(ans,xor)
    for u, w in G[top]:
        if not visited[u]:
            dfs(u,xor^w)
    visited[top]=False
dfs(0,0)
print(ans)
    
    