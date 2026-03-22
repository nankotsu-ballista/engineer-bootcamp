n=int(input())
x,y=map(int,input().split())
INF=10**18
dp=[[INF]*((x+1)*(y+1)) for _ in range(n+1)]
dp[0][0]=0
# for i in dp:
#     print(i)
for i in range(n):
    a,b=map(int,input().split())
    for k in range(((x+1)*(y+1))):
        tako = k // (y + 1)
        tai  = k %  (y + 1)
        ntako = min(x, tako + a)
        ntai  = min(y, tai  + b)
        nxt = ntako * (y + 1) + ntai
        dp[i+1][nxt]=min(dp[i+1][nxt],dp[i][k]+1)
        dp[i+1][k]=min(dp[i+1][k],dp[i][k])
        # if i==1 and k==11:
        #     print(nxt,tako,tai)
# for i in dp:
#     print(i)
ans=INF
for i in range(((x+1)*(y+1))):
    tako=i//(y + 1)
    tai=i%(y + 1)
    #print(tako,tai,dp[n][i])
    if tako>=x and tai>=y:
        ans=min(ans,dp[n][i])
if ans==INF:
    print(-1)
else:
    print(ans)
    

        
        
