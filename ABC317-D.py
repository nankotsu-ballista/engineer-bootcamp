n=int(input())
dp=[10**18]*(10**6)
dp[0]=0
sum=0
for i in range(n):
    x,y,z=map(int,input().split())
    sum+=z
    for j in range((10**5),z-1,-1):
        #print(j)
        if dp[j-z] != 10**18:
            if x>y:
                dp[j]=min(dp[j],dp[j-z])
            else:
                dp[j]=min(dp[j],dp[j-z]+((y-x)//2)+1)
        #print(j)
        
s=sum//2+1
#print(dp[:20])
ans=10**18
#print(s)
for i in range(s,10**6):
    ans=min(dp[i],ans)
print(ans)
    
