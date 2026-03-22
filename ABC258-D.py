from functools import lru_cache
import math
n,x=map(int,input().split())
ans=10**20
sum=0
mininow=10**20
for i in range(n):
    a,b=map(int,input().split())
    sum+=a+b
    mininow=min(mininow,b)
    tmpans=mininow*(x-1-i)+sum
    ans=min(ans,tmpans)
print(ans)