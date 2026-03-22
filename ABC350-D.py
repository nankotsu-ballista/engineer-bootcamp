from collections import deque
N, M = map(int, input().split())
graph = [[] for _ in range(N)]

for _ in range(M):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    graph[a].append(b)
    graph[b].append(a)
visited=[False]*N

def dfs(v):
    stack = [v]
    visited[v] =True
    size = 1
    while stack:
        node = stack.pop()
        for neighbor in graph[node]:
            if not visited[neighbor]:
                visited[neighbor]= True
                stack.append(neighbor)
                size += 1
    return size
    
total_possible_edges = 0
for i in range(N):
    if not visited[i]:
        s= dfs(i)
        total_possible_edges += s *(s-1)//2
print(total_possible_edges-M)