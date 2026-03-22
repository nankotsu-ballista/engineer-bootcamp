n,m,k=map(int,input().split())
mod=998244353
minv = pow(m,mod-2, mod)
dp=[[0]*(n+1) for _ in range(k+1)]
dp[0][0]=1
for i in range(k):
    for j in range(n+1):
        if j==n:
            dp[i+1][j]=(dp[i+1][j]+dp[i][j])%mod
            continue
        for mm in range(1,m+1):
            if j+mm<=n:
                dp[i+1][j+mm]=dp[i+1][j+mm]+dp[i][j]*minv
                dp[i+1][j+mm]=dp[i+1][j+mm]%mod
            if j+mm>n:
                dp[i+1][n-(j+mm-n)]=dp[i+1][n-(j+mm-n)]+dp[i][j]*minv
                dp[i+1][n-(j+mm-n)]=dp[i+1][n-(j+mm-n)]%mod
print(dp[k][n])