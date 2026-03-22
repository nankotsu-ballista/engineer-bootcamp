from itertools import product

S = []
N, K, X = map(int, input().split())
for _ in range(N):
    S.append(input())

# 連結文字列を直接作る
Q = [''.join(p) for p in product(S, repeat=K)]

# 辞書順にソート
Q.sort()

# Xは1-indexed → Pythonは0-indexed
print(Q[X - 1])