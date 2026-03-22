n,m=map(int,input().split())
dp=[[0]*2 for _ in range(n+1)]
dp[1][1]=m
dp[1][0]=0
mod=998244353
for i in range(1,n):
    dp[i+1][0]=(dp[i][1]*(m-1)+dp[i][0]*(m-2))%mod
    dp[i+1][1]=dp[i][0]%mod
print(dp[n][0]%mod)
# for i in dp:
#     print(i)