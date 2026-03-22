n=int(input())
A=list(map(int,input().split()))
dp=[[0]*10 for _ in range(n+1)]
dp[1][A[0]]+=1
for i in range(1,n):
    for k in range(10):
        dp[i+1][k*A[i]%10]+=dp[i][k]
        dp[i+1][(k+A[i])%10]+=dp[i][k]
    for k in range(10):
        dp[i+1][k]=dp[i+1][k]%998244353
        dp[i+1][k]=dp[i+1][k]%998244353
for i in range(10):
    print(dp[n][i])
