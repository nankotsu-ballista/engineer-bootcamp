n=int(input())
dp=[0]*(n+1)
dp[0]=3.5
for i in range(n):
    kitai=0
    for k in range(1,7):
        if k>dp[i]:
            kitai+=1/6*k
        else:
            kitai+=1/6*dp[i]
    dp[i+1]=kitai
print(dp[n-1])
    