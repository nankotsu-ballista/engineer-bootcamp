from collections import deque

def bfs(start, graph, n):
    dist = [-1] * (n + 1)
    queue = deque([start])
    dist[start] = 0
    while queue:
        node = queue.popleft()
        for neighbor in graph[node]:
            if dist[neighbor] == -1:
                dist[neighbor] = dist[node] + 1
                queue.append(neighbor)
    return dist

def main():
    N1, N2, M = map(int, input().split())
    N = N1 + N2
    graph = [[] for _ in range(N + 1)]

    for _ in range(M):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    dist1 = bfs(1, graph, N)
    distN = bfs(N, graph, N)

    maxA = max(dist1[1:N1+1])
    maxB = max(distN[N1+1:N+1])

    print(maxA + 1 + maxB)

main()