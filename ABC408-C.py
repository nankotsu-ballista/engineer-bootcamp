N, M = map(int, input().split())
houdai = [0] * (N + 1)  # R まで使うから +1
#print(houdai)
for _ in range(M):
    L, R = map(int, input().split())
    houdai[L - 1] += 1
    houdai[R] -= 1  # R の1つ後ろに -1（ここが修正ポイント）
#(houdai)

# 累積和
for i in range(1, N):
    houdai[i] += houdai[i - 1]

# 最小値探索（0〜N-1まで）
print(min(houdai[:N]))
