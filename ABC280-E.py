n,p=map(int,input().split())
if n==1:
    print(1)
    exit()

mod=998244353
dp=[0]*(n+2)
#print(dp)
hinv=pow(100,mod-2,mod)
a=p*hinv%mod
b=(100-p)*hinv%mod
dp[0]=0
dp[1]=1
for i in range(2,n+1):
    dp[i]=(1+a*dp[i-2]+b*dp[i-1])%mod
#print(dp)
print(dp[n])