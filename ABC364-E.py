n,x,y=map(int,input().split())
dp=[[[10**5+1]*(n+1) for _ in range(x+1)]for _ in range(n+1)]
dp[0][0][0]=0
for i in range(n):
    a,b=map(int,input().split())
    for j in range(x+1):
        for k in range(n):
            dp[i+1][j][k] = min(dp[i+1][j][k], dp[i][j][k])
            if j+a>x or dp[i][j][k]+b>y:
                continue
            dp[i+1][j+a][k+1]=min(dp[i][j][k]+b,dp[i+1][j+a][k+1])
# for i in dp:
#     print(i)
ans=0
for i in range(x+1):
    for k in range(n+1):
        if dp[n][i][k]!=10**5+1:
            ans=max(ans,k)
print(min(n,ans+1))