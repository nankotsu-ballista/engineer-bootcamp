import math
from math import lcm
n,m,k=map(int,input().split())
s=(math.lcm(n, m))
l=1
r=10**18
while l<r:
    mid=(r+l)//2
    t = mid//n + mid//m-(mid//s)*2
    #print(t)
    if t<k:
        l=mid+1
    else:
        r=mid
print(l)