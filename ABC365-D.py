n=int(input())
s=input()
dp=[[0]*3 for _ in range(n)]
if s[0] =="R":
    dp[0][2]+=1
if s[0] =="S":
    dp[0][0]+=1
if s[0] =="P":
    dp[0][1]+=1
for i in range(1,n):
    if s[i]=="R":
        dp[i][0]=max(dp[i-1][1],dp[i-1][2])
        dp[i][2]=max(dp[i-1][1]+1,dp[i-1][0]+1)
    elif s[i]=="S":
        dp[i][0]=max(dp[i-1][1]+1,dp[i-1][2]+1)
        dp[i][1]=max(dp[i-1][0],dp[i-1][2])
    elif s[i]=="P":
        dp[i][1]=max(dp[i-1][2]+1,dp[i-1][0]+1)
        dp[i][2]=max(dp[i-1][1],dp[i-1][0])
print(max(dp[n-1][0],dp[n-1][1],dp[n-1][2]))

    