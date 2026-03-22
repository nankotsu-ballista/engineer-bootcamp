n=int(input())
A=list(map(int,input().split()))
dp=[[10**18]*(n) for _ in range(2)]
dp[0][0]=0
dp[1][0]=10**18
ans=10**18
for i in range(n-1):
    dp[0][i+1]=dp[1][i]
    dp[1][i+1]=min(dp[1][i]+A[i+1],dp[0][i]+A[i+1])
# for i in dp:
#     print(i)
ans=min(ans,dp[1][n-1])
dp[0][0]=10**18
dp[1][0]=A[0]
for i in range(n-1):
    dp[0][i+1]=dp[1][i]
    dp[1][i+1]=min(dp[1][i]+A[i+1],dp[0][i]+A[i+1])
# for i in dp:
#     print(i)
ans=min(ans,dp[0][n-1],dp[1][n-1])
print(ans)


