n=int(input())
tmp=0
b=1
while b<=n:
    q=n//b
    r= n//q
    tmp += q*(r-b+1)
    b = r+1
    tmp-tmp%998244353
ans=n*(n+1)//2-tmp
print(ans%998244353)