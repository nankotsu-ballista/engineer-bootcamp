n=int(input())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
dp=[[0]*(b[-1]+1) for _ in range(n+1)]
for i in range(a[0],b[0]+1):
    dp[1][i]=1
#print(dp)
for i in range(1,n):
    #print(i)
    dp[i+1][a[i]]=sum(dp[i][:a[i]])
    summ=sum(dp[i][:a[i]])
    for k in range(a[i],b[i]+1):
        summ+=dp[i][k]
        dp[i+1][k]=summ%998244353
ans=0
for i in range(b[-1]+1):
    ans+=dp[n][i]
    ans=ans%998244353
print(ans)
    
    
        
        