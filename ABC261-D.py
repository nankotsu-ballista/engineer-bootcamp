from collections import defaultdict,deque
n,m=map(int,input().split())
x=list(map(int,input().split()))
bonus=[0]*5001
for i in range(m):
    c,y=map(int,input().split())
    bonus[c]=y
dp=[[-10**18]*(n+1) for _ in range(n+1)]
dp[0][0]=0
for i in range(n):
    for k in range(n):
        dp[i+1][k+1]=max(dp[i][k]+bonus[k+1]+x[i],dp[i+1][k+1])
        dp[i+1][0]=max(dp[i][k],dp[i+1][0])
print(max(dp[n]))