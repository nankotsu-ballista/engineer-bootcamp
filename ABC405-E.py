a,b,c,d=map(int,input().split())
MOD = 998244353
nmax=a+b+c+d
kaijou=[0]*(nmax+1)
gyakukaijou=[0]*(nmax+1)
kaijou[0]=1
for i in range(1,nmax+1):
    kaijou[i]=kaijou[i-1]*i%MOD
#print(kaijou)
gyakukaijou[nmax] = pow(kaijou[nmax], MOD-2, MOD)
for i in range(nmax-1,-1,-1):
    gyakukaijou[i]=gyakukaijou[i+1]*(i+1)%MOD
#print(gyakukaijou)
ans=0
for i in range(c+1):
    tmp1=kaijou[a+i+b]*gyakukaijou[a+i]*gyakukaijou[b]%MOD
    tmp2=kaijou[d-1+c-i]*gyakukaijou[c-i]*gyakukaijou[d-1]%MOD
    ans=(ans+tmp1*tmp2)%MOD
print(ans)