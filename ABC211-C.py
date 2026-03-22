MOD = 10**9 + 7
S = input().strip()
T = "chokudai"

dp = [0] * (len(T) + 1)
dp[0] = 1  # 空文字は1通り

for ch in S:
    for j in (range(len(T))):  # 後ろから見ないと上書きされる
        if ch == T[j]:
            dp[j+1] = (dp[j+1] + dp[j]) % MOD

print(dp[8])  # chokudai 全体ができる通り数
