from functools import lru_cache
import math,bisect,heapq
from collections import deque
s=input()
k=int(input())
s=list(s)
ruiseki=[0]
sum=0
ans=0
for i in range(len(s)):
    if s[i]==".":
        sum+=1
    ruiseki.append(sum)
#print(ruiseki)
for i in range(len(s)):
    idx=bisect.bisect_right(ruiseki,ruiseki[i]+k)
    ans=max(ans,idx-i-1)
print(ans)