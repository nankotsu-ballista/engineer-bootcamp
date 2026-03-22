t,mod=map(int,input().split())
M = 10**9+7  # 問題の指定に合わせて変える
dp=[[0]*5001 for _ in range(5001)]
dp[0][0]=1
for n in range(1,5001):
    dp[n][0]=1
    for k in range(1,n+1):
        dp[n][k]=(dp[n-1][k-1]+dp[n-1][k])%mod
for _ in range(t):
    #print(kaijous)
    n=int(input())
    C=list(map(int,input().split()))
    ans=1
    s=0
    for c in C:
      s+=c
      ans=ans*dp[s][c]%mod
    print(ans)