N,M=map(int,(input().split()))
graph = [[0] * (N + 1) for _ in range(N + 1)]
for _ in range(M):
    a,b,c = map(int,input().split())
    graph[a][b] = c
    graph[b][a] = c
    
visited = [False] * (N + 1)

ans= 0
 
def dfs(v,cost):
    global ans
    visited[v] = True
    ans = max(ans, cost)
    
    for i in range(1,N+1):
        if not visited[i] and graph[v][i] > 0:
            dfs(i,cost+ graph[v][i])
    
    visited[v]=False
    
for start in range(1,N+1):
    dfs(start,0)
    
print(ans)