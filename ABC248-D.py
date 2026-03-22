from functools import lru_cache
import math,bisect
n=int(input())
A=list(map(int,input().split()))
q=int(input())
numidxs=[[] for _ in range(2*10**5+1)]
for i in range(n):
    numidxs[A[i]].append(i)
#print(numidxs[:10])
for i in range(q):
    l,r,x=map(int,input().split())
    l-=1
    r-=1
    lidx=bisect.bisect_left(numidxs[x],l)
    ridx=bisect.bisect_right(numidxs[x],r)
    #print(ridx,lidx)
    print(ridx-lidx)