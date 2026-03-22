from collections import defaultdict

N = int(input())
A = list(map(int, input().split()))

# 1. 出現回数を数える（連想配列）
count = defaultdict(int)
for a in A:
    count[a] += 1

# 2. 一意な値を探す
max_val = -1
index = -1
for i in range(N):
    if count[A[i]] == 1:  # 自分だけが持っている数
        if A[i] > max_val:
            max_val = A[i]
            index = i + 1  # 人の番号は1-indexed

print(index if index != -1 else -1)
