n,x=map(int,input().split())
items=[]
score=[]
cost=[]
kakuritu=[]

for i in range(n):
    s,c,p=map(int,input().split())
    score.append(s)
    cost.append(c)
    kakuritu.append(p)
dp=[[0]*(x+1) for _ in range(2**n)]
for tt in range(x+1):
    for i in range(2**n):
        for k in range(n):
            if 1<<k & i:
                if i-2**k<0:
                    continue
                if cost[k]+tt<x+1:
                    dp[i-2**k][cost[k]+tt]=max(dp[i-2**k][cost[k]+tt],(dp[i][tt]+score[k])*(kakuritu[k]/100)+dp[i-2**k][tt]*((100-kakuritu[k])/100))
ans=0

for i in dp:
    ans=max(ans,i[-1])
print(ans)