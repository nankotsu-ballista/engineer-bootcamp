import math
n=int(input())
P=list(map(int,input().split()))
P.reverse()
dp=[[0]*(n+1) for _ in range(n+1)]
for i in range(n):
    for k in range(i+1):
        dp[i+1][k+1]=max(dp[i+1][k+1],dp[i][k]+(0.9)**k*(P[i]))
        dp[i+1][k+1]=max(dp[i+1][k+1],dp[i][k+1])
# for i in dp:
#     print(i)
ans=-10**18
bunbos=[0]*5001
bunbo=0
for i in range(5001):
    bunbo=bunbo+(0.9)**i
    bunbos[i]=bunbo
#print(bunbos)
for i in range(1,n+1):
    bunshi=dp[n][i]
    sabun=1200/math.sqrt(i)
    #print(bunshi,bunbos[i-1],sabun)
    ans=max(ans,bunshi/bunbos[i-1]-sabun)
print(ans)
    