import heapq
n,m,k=map(int,input().split())
nodes=[[] for _ in range(n)]
for i in range(m):
    u,v=map(int,input().split())
    nodes[u-1].append(v-1)
    nodes[v-1].append(u-1)
dp=[[0]*n for _ in range(k+1)]
dp[0][0]=1
for i in range(k):
    sum=0
    for j in range(n):
        sum+=dp[i][j]%998244353
    for j in range(n):
        dp[i+1][j]=sum
    for j in range(n):
        for p in nodes[j]:
            dp[i+1][j]=(dp[i+1][j]-dp[i][p])%998244353
        dp[i+1][j]=(dp[i+1][j]-dp[i][j])%998244353
        
print(dp[k][0])
        
        
        