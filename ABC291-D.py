n=int(input())
cards=[]
cards.append((-1,-1))
for i in range(n):
    a,b=map(int,input().split())
    cards.append((a,b))
#print(cards)
dp=[[0]*2 for i in range(n+1)]
dp[1][1]=1
dp[1][0]=1
for i in range(1,n):
    if cards[i][0]!=cards[i+1][0]:
        dp[i+1][0]=(dp[i+1][0]+dp[i][0])%998244353
    if cards[i][1]!=cards[i+1][0]:
        dp[i+1][0]=(dp[i+1][0]+dp[i][1])%998244353
    if cards[i][1]!=cards[i+1][1]:
        dp[i+1][1]=(dp[i+1][1]+dp[i][1])%998244353
    if cards[i][0]!=cards[i+1][1]:
        dp[i+1][1]=(dp[i+1][1]+dp[i][0])%998244353
#print(dp)       
        
print((dp[n][0]+dp[n][1])%998244353)