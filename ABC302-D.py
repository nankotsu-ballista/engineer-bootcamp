import bisect

N, M, D = map(int, input().split())
A = list(map(int, input().split()))
B = sorted(map(int, input().split()))  # B は二分探索するのでソート

ans = -1

for a in A:
    upper = a + D
    lower = a - D

    # B[j] <= upper を満たす最大のインデックスを探す
    idx = bisect.bisect_right(B, upper) - 1

    if idx >= 0 and B[idx] >= lower:
        total = a + B[idx]
        ans = max(ans, total)

print(ans)