import itertools,heapq
from collections import deque
n,m=map(int,input().split())
s=set()
for i in range(400):
    b=(m-i**2)
    if b<0:
        break
    bb=b**(1/2)
    if b-int(bb)**2==0:
        s.add((i,int(bb)))
        s.add((-i,int(bb)))
        s.add((i,-int(bb)))
        s.add((-i,-int(bb)))
q=[]
#print(s)
heapq.heappush(q,(0,0,0))
reach=set()
s=list(s)
count=0
grid=[[-1]*n for _ in range(n)]
grid[0][0]=0
reach.add((0,0))
#print(s)
while q:
    #print(q)
    time,ii,k=heapq.heappop(q)

    for i in range(len(s)):
        di,dk=s[i]
        if (ii+di,k+dk) not in reach and 0<=ii+di<n and 0<=k+dk<n:
            grid[ii+di][k+dk]=time+1
            reach.add((ii+di,k+dk))
            heapq.heappush(q,(time+1,ii+di,k+dk))
for i in grid:
    print(*i)
    

