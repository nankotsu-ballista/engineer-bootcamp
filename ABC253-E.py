from collections import deque
import heapq
n,m,k=map(int,input().split())
dp=[[0]*(m+1) for _ in range(n+1)]
if k==0:
    print(m**n%998244353)
    exit()
for i in range(m+1):
    dp[1][i]=1
dp[1][0]=0
for i in range(1,n):
    sums=[]
    sumq=0
    for tt in range(m+1):
        sumq+=dp[i][tt]
        sums.append(sumq)
    # print("sums",sums)
    for j in range(1,m+1):
        dp[i+1][j]=(sums[max(0,j-k)]+dp[i+1][j])%998244353
        dp[i+1][j]=(sums[-1]-sums[min(j+k-1,m)]+dp[i+1][j])%998244353
# for i in dp:
#     print(i)
print(sum(dp[n])%998244353)
            