from collections import deque

N, M = map(int, input().split())
S = input()
C = list(map(int, input().split()))

Lo = [deque() for _ in range(M+1)]
for i in range(N):
    Lo[C[i]].append(S[i])

for i in range(M+1):
    if Lo[i]:
        Lo[i].appendleft(Lo[i].pop())  # 右回転1回（先頭を末尾に）

ans = ""
for i in range(N):
    ans += Lo[C[i]].popleft()

print(ans)
