n,k=map(int,input().split())
dp=[0]*(10**5+1)
MOD=998244353
dp[0]=1
invN=pow(n, MOD-2, MOD)%MOD
inv2=pow(2, MOD-2, MOD)%MOD
p=2*(n-1)*invN*invN%MOD
q=2*invN*invN%MOD
for i in range(10**5):
    
    dp[i+1]+=dp[i]*(1-p)%MOD
    dp[i+1]+=(1-dp[i])%MOD*q
    dp[i+1]=dp[i+1]%MOD
ans=dp[k]+(1-dp[k])*(n+2)*inv2
ans=ans%MOD
print(ans)