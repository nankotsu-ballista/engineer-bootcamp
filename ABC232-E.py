h,w,k=map(int,input().split())
x1,y1,x2,y2=map(int,input().split())
dp=[[[0]*(2) for _ in range(2)]for _ in range(k+1)]
mod=998244353
c=0
d=0
if x1==x2:
    c=1
if y1==y2:
    d=1
dp[0][c][d]=1
for i in range(k):
    dp[i+1][1][0]=(dp[i][0][0]+dp[i][1][1]*(w-1)+dp[i][1][0]*(w-2))%mod
    dp[i+1][1][1]=(dp[i][1][0]+dp[i][0][1])%mod
    dp[i+1][0][0]=(dp[i][1][0]*(h-1)+dp[i][0][1]*(w-1)+dp[i][0][0]*(h-2)+dp[i][0][0]*(w-2))%mod
    dp[i+1][0][1]=(dp[i][0][0]+dp[i][1][1]*(h-1)+dp[i][0][1]*(h-2))%mod


print(dp[k][1][1])
