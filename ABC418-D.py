N=int(input())
T=input()
T=list(T)
#print(T)
dp=[[0]*(N+1) for _ in range(2)]
for i in range(N):
    if T[i] == "0":
        dp[0][i+1]=dp[1][i]
        dp[1][i+1]=dp[0][i]+1
    else:
        dp[0][i+1]=dp[0][i]+1
        dp[1][i+1]=dp[1][i]
ans=0
for i in range(N+1):
    ans+=dp[0][i]
print(ans)