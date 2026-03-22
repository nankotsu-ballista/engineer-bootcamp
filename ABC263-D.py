n,l,r=map(int,input().split())
a=list(map(int,input().split()))
lsum=0
rsum=0
ans=0
sun=0
for i in range(n):
    sun+=a[i]
R=[]
a.reverse()
for i in range(n):
    R.append(rsum)
    rsum+=r-a[i]
R.append(rsum)
R.reverse()
a.reverse()
#R=[0]+R
#print(R)
true=0
for i in range(n):
    lsum+=l-a[i]
    ans=min(ans,lsum)
    #print(i,lsum)
    true=min(true,ans+R[i+1])
ss=0
ass=0
for i in range(n):
    ss+=l-a[i]
    ass=min(ss,ass)
    #print(ss)
a.reverse()
kss=0
kass=0
for i in range(n):
    kss+=r-a[i]
    kass=min(kss,kass)
    #print(ss)
print(min((sun+true),(sun+ass),(sun+kass)))