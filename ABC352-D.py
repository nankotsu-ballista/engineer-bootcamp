import sys, heapq

it = iter(map(int, sys.stdin.buffer.read().split()))
n = next(it); k = next(it)
p = [next(it) for _ in range(n)]

pos = [0]*n                     # pos[v-1] = 値 v の出現位置
for i, v in enumerate(p):
    pos[v-1] = i

if k == 1:
    print(0)
    raise SystemExit

min_h, max_h = [], []           # 最小ヒープ / 最大は負で詰める
present = [False]*n             # 位置が現在の集合に含まれるか

# 初期ウィンドウ {1..k} の出現位置を投入（0-index -> 0..k-1）
for a in range(k):
    x = pos[a]
    present[x] = True
    heapq.heappush(min_h, x)
    heapq.heappush(max_h, -x)

# 先頭を掃除してから差を取る
while min_h and not present[min_h[0]]:
    heapq.heappop(min_h)
while max_h and not present[-max_h[0]]:
    heapq.heappop(max_h)
ans = (-max_h[0]) - min_h[0]

# a をスライド（入れ替え：pos[a-k] を無効化→ pos[a] を追加）
for a in range(k, n):
    out = pos[a-k]; present[out] = False
    inn = pos[a];   present[inn] = True
    heapq.heappush(min_h, inn)
    heapq.heappush(max_h, -inn)

    while min_h and not present[min_h[0]]:
        heapq.heappop(min_h)
    while max_h and not present[-max_h[0]]:
        heapq.heappop(max_h)

    diff = (-max_h[0]) - min_h[0]
    if diff < ans:
        ans = diff

print(ans)
