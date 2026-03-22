from collections import defaultdict
import heapq
n,d=map(int,input().split())
lr=defaultdict(list)
rlist=[]
llist=[]
broken=set()
for i in range(n):
    l,r=map(int,input().split())
    heapq.heappush(rlist,(r,i))
    heapq.heappush(llist,(l,i))
    lr[i]=(l,r)
rlist.sort()
count=0
# print(rlist)
# print(llist)
while rlist:
    rr,idx=heapq.heappop(rlist)
    if idx in broken:
        continue
    count+=1
    broken.add(idx)
    while llist:
        ll,idx=heapq.heappop(llist)
        if ll<=rr+d-1:
            broken.add(idx)
        else:
            heapq.heappush(llist,(ll,idx))
            break
print(count)
    