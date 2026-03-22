MOD = 998244353
s=input()
s=list(s)
n=len(s)
dp = dp = [[0] * (n + 1) for _ in range(n + 1)]
dp[0][0]=1
for i in range(n):
    for j in range(n):
        if dp[i][j]== 0:
            continue
        if s[i]!=")":
            dp[i+1][j+1]=(dp[i+1][j+1]+dp[i][j])%MOD
        if s[i]!="("and j!=0:
            dp[i+1][j-1]=(dp[i+1][j-1]+dp[i][j])%MOD
#print(dp)
print(dp[n][0]%MOD)