from functools import lru_cache
import math,bisect
n,q=map(int,input().split())
A=list(map(int,input().split()))
sums=[0]
sum=0
A.sort()
for i in A:
    sum+=i
    sums.append(sum)
# print(A)
# print(sums)
for i in range(q):
    x=int(input())
    idx=bisect.bisect_left(A,x)
    ans=idx*x-sums[idx]+(sum-sums[idx])-x*(n-idx)
    #print(idx,sums[idx])
    print(ans)