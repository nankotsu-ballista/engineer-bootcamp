n, k = map(int, input().split())
MOD = 10**9

# A[0] ~ A[k-1] = 1
a = [1] * (n + 1)

# 初期和 S = A[0] + A[1] + ... + A[k-1] = k
s = k

# A[k] ~ A[n] を順に計算
for i in range(k, n + 1):
    a[i] = s
    s -= a[i - k]  # ウィンドウ左端を除外
    s += a[i]      # 新しいA[i]を追加
    s %= MOD       # オーバーフロー対策

print(a[n])
