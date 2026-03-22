from functools import lru_cache
import math,bisect,heapq
from collections import deque,defaultdict
n,p,q,r=map(int,(input().split()))
a=list(map(int,(input().split())))
ruiseki=[0]
sum=0
for i in range(len(a)):
    sum+=a[i]
    ruiseki.append(sum)
#print(ruiseki)
for i in range(n-2):
    ruiseki[i]
    idx1=bisect.bisect_left(ruiseki,ruiseki[i]+p)
    if idx1==n+1:
        continue
    idx2=bisect.bisect_left(ruiseki,ruiseki[idx1]+q)
    if idx2==n+1:
        continue
    idx3=bisect.bisect_left(ruiseki,ruiseki[idx2]+r)
    if idx3==n+1:
        continue
    #print(i,idx1,idx2,idx3)
    if ruiseki[idx3]-ruiseki[idx2]==r and ruiseki[idx2]-ruiseki[idx1]==q and ruiseki[idx1]-ruiseki[i]==p:
        print("Yes")
        exit()
print("No")