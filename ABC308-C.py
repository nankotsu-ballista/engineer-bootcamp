from functools import cmp_to_key

n = int(input())
ab = []
for _ in range(n):
    a, b = map(int, input().split())
    ab.append((a, a + b))  # (a, a + b) を保持

p = list(range(n))  # インデックス配列 [0, 1, 2, ..., n-1]

# 比較関数：ab[i], ab[j] の大小比較
def cmp(i, j):
    ai, aib = ab[i]
    aj, ajb = ab[j]
    # 注意：long long 相当でオーバーフローしないようにする
    if ai * ajb > aj * aib:
        return -1
    elif ai * ajb < aj * aib:
        return 1
    else:
        return 0  # 安定ソート維持

# 安定ソート
p.sort(key=cmp_to_key(cmp))

# 出力（1-indexed）
print(' '.join(str(x + 1) for x in p))