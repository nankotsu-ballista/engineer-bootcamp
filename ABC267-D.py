n,m=map(int,input().split())
a=list(map(int,input().split()))
sum=0
dp=[[-10**20]*(n+1) for _ in range(n+1)]
dp[0][0]=0
for i in range(n):
    for k in range(n):
        dp[i+1][k]=max(dp[i][k],dp[i+1][k])
        dp[i+1][k+1]=max(dp[i+1][k+1],dp[i][k]+(k+1)*a[i])
# for i in dp:
#     print(i)
print(dp[n][m])