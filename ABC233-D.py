from functools import lru_cache
import math,bisect,heapq
from collections import deque,defaultdict

n,k=map(int,input().split())
a=list(map(int,input().split()))
sum=0
ruiseki=[0]
numscount=defaultdict(list)
for i in range(n):
    sum+=a[i]
    ruiseki.append(sum)
#print(ruiseki)
for i in range(n+1):
    numscount[ruiseki[i]].append(i)
#print(numscount)
for i in numscount:
    numscount[i].sort()
ans=0
for i in range(n):
    if numscount[k+ruiseki[i]]:
        #print(i,bisect.bisect_left(numscount[k+ruiseki[i]],i))
        idx=(bisect.bisect_right(numscount[k+ruiseki[i]],i))
        ans+=(len(numscount[k+ruiseki[i]])-idx)
print(ans)
    
    