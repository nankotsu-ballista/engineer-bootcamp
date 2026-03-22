n=int(input())
dp=[[-10**18]*5 for _ in range(10**5+1)]
dp[0][0]=0
count=0
mogura=[[] for _ in range(10**5+1)]
for i in range(n):
    t,x,a=map(int,input().split())
    mogura[t]=(x,a)
for i in range(10**5):
    for k in range(5):
        dp[i+1][k]=max(dp[i][max(k-1,0)],dp[i][min(k+1,4)],dp[i][k])
    if mogura[i+1]:
        x,a=mogura[i+1]
        dp[i+1][x]+=a
print(max(dp[10**5]))