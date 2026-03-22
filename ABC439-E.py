import heapq
import bisect
from collections import defaultdict
n=int(input())
d=defaultdict(list)
s=set()
items=[]

for i in range(n):
    a,b=map(int,input().split())
    d[a].append(b)
#print(d)
d = sorted(d.items())
#print(d)
for i in range(len(d)):
    #print(d[i])
    d[i][1].sort()
    d[i][1].reverse()
    for f in d[i][1]:
        items.append(f)
#print(items)
ans=0
itemss=items
dp=[itemss[0]]
#print(dp)
for i in range(1,len(items)):
    idx=bisect.bisect_left(dp,itemss[i])
    if idx<len(dp):
        dp[idx]=itemss[i]
    else:
        dp.append(itemss[i])
print(len(dp))