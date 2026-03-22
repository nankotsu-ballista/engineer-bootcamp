N=int(input())
dp = [[0 for _ in range(N+1)] for _ in range(2)]
for i in range(N):
    X,Y =map(int,input().split())
    if X==0:
        dp[0][i+1]=max(dp[0][i]+Y,dp[0][i],dp[1][i]+Y)
        dp[1][i+1]=dp[1][i]
    elif X==1:
        dp[0][i+1]=dp[0][i]
        dp[1][i+1]=max(dp[0][i]+Y,dp[1][i])
print(max(dp[0][N],dp[1][N]))
        