n, m = map(int, input().split())
s = [input() for _ in range(n)]

ans = n  # 最悪ケース（全部行く）

for bit in range(1 << n):  # 2^n 通り
    exist = [False] * m    # 味がカバーされてるかどうか
    cnt = 0  # 選んだ売り場数

    for i in range(n):
        if bit >> i & 1:
            cnt += 1
            for j in range(m):
                if s[i][j] == 'o':
                    exist[j] = True

    if all(exist):  # すべての味をカバーしているか
        ans = min(ans, cnt)

print(ans)