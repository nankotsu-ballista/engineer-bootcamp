s=input()
N=int(input())
dp=[[10**18]*(len(s)+1) for _ in range(N+1)]
for i in range(N):
    dp[i][0]=0
for i in range(N):
    Q=list(map(str,input().split()))
    A=int(Q[0])
    for j in range(A):
        S=Q[j+1]
        for k in range(len(s)-len(S)+1):
            if s[k:k+len(S)]==S:
                dp[i+1][k+len(S)]=min(dp[i][k]+1,dp[i+1][k+len(S)])
            #print(s[k:k+len(S)],S)
        for k in range(len(s)+1):
            dp[i+1][k]=min(dp[i+1][k],dp[i][k])
#print(dp)
if dp[N][len(s)]==10**18:
    print(-1)
else:
    print(dp[N][len(s)])
