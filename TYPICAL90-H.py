import bisect
n=int(input())
s=input()
s=list(s)
dp=[[0]*7 for _ in range(n+1)]
moji=["a","t","c","o","d","e","r"]
for i in range(n):
    if s[i]=="a":
        dp[i+1][0]=max(dp[i+1][0],dp[i][0]+1)
    elif s[i]=="r":
        dp[i+1][6]=max(dp[i][6]+dp[i][5],dp[i+1][6])
    elif s[i]=="t":
        dp[i+1][1]=max(dp[i][1]+dp[i][0],dp[i+1][1])
    elif s[i]=="c":
        dp[i+1][2]=max(dp[i][2]+dp[i][1],dp[i+1][2])
    elif s[i]=="o":
        dp[i+1][3]=max(dp[i][3]+dp[i][2],dp[i+1][3])
    elif s[i]=="d":
        dp[i+1][4]=max(dp[i][4]+dp[i][3],dp[i+1][4])
    elif s[i]=="e":
        dp[i+1][5]=max(dp[i][5]+dp[i][4],dp[i+1][5])
    for k in range(7):
        dp[i+1][k]=max(dp[i][k],dp[i+1][k])%(10**9+7)
#for i in dp:
    #print(i)
print(dp[n][6]%(10**9+7))
        
    