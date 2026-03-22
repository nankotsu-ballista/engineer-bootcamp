from collections import defaultdict
n,m=map(int,input().split())
A=list(map(int,input().split()))
mods=defaultdict(lambda: defaultdict(int))
for k in A:
    for i in range(1,11):
        mods[i][(10**i)*k%m]+=1
        #print((10**i)*k%m)
ans=0
for i in A:
    amari=i%m
    leng=len(str(i))
    #print(leng)
    ans+=mods[leng][m-amari]
    if amari==0:
        ans+=mods[leng][0]
print(ans)