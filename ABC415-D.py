n, m = map(int, input().split())
ls = []

for _ in range(m):
    a, b = map(int, input().split())
    d = a - b
    ls.append((d, a, b))

ls.sort()  # D[i]の昇順にソート

ans = 0
for d, a, b in ls:
    if a > n:
        continue
    x = (n - a) // d + 1  # 操作可能な最大回数
    #rint(x)
    ans += x
    n -= x * d  # N を更新（D[i] × x 引く）

print(ans)