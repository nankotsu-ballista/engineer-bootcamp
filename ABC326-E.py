n=int(input())
A=list(map(int,input().split()))
psum=1/3
p=0
plist=[]
MOD = 998244353
invN = pow(n, MOD-2, MOD)
psum=pow(n, MOD-2, MOD)
for i in range(1,n+1):
    plist.append(psum)
    psum+=psum*(invN)
    psum=psum%MOD
#print(plist)
ans=0
for i in range(n):
    ans+=A[i]*plist[i]
    ans=ans%MOD
print(ans)