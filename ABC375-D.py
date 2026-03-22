import sys

s = sys.stdin.readline().strip()

cnt = [0] * 26
sum_idx = [0] * 26
ans = 0

for i, ch in enumerate(s):
    v = ord(ch) - ord('A')
    ans += (i - 1) * cnt[v] - sum_idx[v]
    cnt[v] += 1
    sum_idx[v] += i

print(ans)
