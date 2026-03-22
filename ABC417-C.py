from collections import defaultdict

N = int(input())
A = list(map(int, input().split()))

count = defaultdict(int)
ans = 0

for i in range(N):
    # j - A[j] == i + A[i] を探す（i < j）
    ans += count[i - A[i]]
    # この i を、次の j のために追加
    count[i + A[i]] += 1

print(ans)