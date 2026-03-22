N = int(input())
S = input()

c1 = S.count('1')  # 全体の1の数
now = 0            # 今までに見た1の数（左側の1の数）
ans = 0

for c in S:
    if c == '0':
        ans += min(now, c1 - now)
    else:
        now += 1

print(ans)