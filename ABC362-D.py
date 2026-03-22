import sys, heapq
input = sys.stdin.readline

n, m = map(int, input().split())
a = list(map(int, input().split()))
node = [[] for _ in range(n)]
for _ in range(m):
    u, v, b = map(int, input().split())
    u -= 1; v -= 1
    node[u].append((v, b))
    node[v].append((u, b))

h = [(a[0], 0)]          # 始点コストは A[0]
dist = [0]*n
check = [False]*n
nowcost = [10**18]*n
nowcost[0] = a[0]

done = 0
while h:
    cost, point = heapq.heappop(h)
    if cost != nowcost[point]:    # 古い候補は捨てる（重要）
        continue
    if check[point]:
        continue

    check[point] = True
    dist[point] = cost
    if point != 0:
        done += 1
        if done == n-1:           # 1以外が全部確定したら出力
            print(*dist[1:])
            sys.exit()

    for nxt, cos in node[point]:
        if check[nxt]:
            continue
        nd = cost + cos + a[nxt]  # 到着側のAを加算
        if nd < nowcost[nxt]:     # 緩和成功時だけpush
            nowcost[nxt] = nd
            heapq.heappush(h, (nd, nxt))
