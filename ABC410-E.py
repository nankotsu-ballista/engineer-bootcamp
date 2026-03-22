from collections import deque
n,h,m=map(int,input().split())
dp=[[-1]*3001 for _ in range(n+1)]
dp[0][m]=h
for i in range(n):
    a,b=map(int,input().split())
    for k in range(3001):
        if dp[i][k]>=a:
            dp[i+1][k]=max(dp[i+1][k],dp[i][k]-a)
        if k>=b and dp[i][k]>-1:
            dp[i+1][k-b]=max(dp[i+1][k-b],dp[i][k])
for i in range(n+1):
    for k in range(3001):
        if dp[i][k]!=-1:
            ans=i
print(ans)

    
    