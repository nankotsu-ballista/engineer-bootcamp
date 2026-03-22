from collections import deque
import heapq
n,m,k,s,t,x=map(int,input().split())
dp=[ [[0]*2 for _ in range(n+1) ]for _ in range(k+1)]
nodes=[[] for _ in range(n+1)]
for i in range(m):
    u,v=map(int,input().split())
    nodes[u].append(v)
    nodes[v].append(u)
dp[0][s][0]=1
for i in range(k):
    for j in range(n+1):
        for l in nodes[j]:
            if l!=x:
                dp[i+1][l][0]=(dp[i+1][l][0]+dp[i][j][0])%998244353
                dp[i+1][l][1]=(dp[i+1][l][1]+dp[i][j][1])%998244353
            else:
                dp[i+1][l][0]=(dp[i+1][l][0]+dp[i][j][1])%998244353
                dp[i+1][l][1]=(dp[i+1][l][1]+dp[i][j][0])%998244353
# for i in dp:
#     print(i)
print(dp[k][t][0])