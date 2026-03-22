from collections import defaultdict,deque
import heapq
n,q=map(int,input().split())
a=list(map(int,input().split()))
s=defaultdict(int)
se=set()#tuk
for k in a:
    s[k]+=1
    se.add(k)
#print(s)
c=[]
k=0
count=0
SET=set()
while count<2*10**5+1:
    if k in se:
        k+=1
    else:
        heapq.heappush(c, (k))
        SET.add(k)
        count+=1
        k+=1
        
        
for k in range(q):
    i,x=map(int,input().split())
    s[a[i-1]]-=1
    if s[a[i-1]]==0:
        se.discard(a[i-1])
        heapq.heappush(c, (a[i-1]))
    s[x]+=1
    if s[x]==1:
        se.add(x)
    a[i-1]=x
    # print(s)
    # print(c)
    # print(se)
    # print(a)
    while True:
        ans=heapq.heappop(c)
        if ans not in se:
            print(ans)
            heapq.heappush(c, ans)
            break
        
    
    
    
