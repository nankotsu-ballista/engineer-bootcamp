import heapq
n,m=map(int,input().split())
hq=[]
backing=[]
for i in range(n):
    heapq.heappush(hq,(i))
eat=[0]*n
# print(hq)
# print(eat)
nowtime=0
for i in range(m):
    #print(hq)
    t,w,s=map(int,input().split())
    while backing:
        time,humanid=heapq.heappop(backing)
        if time>t:
            heapq.heappush(backing,(time,humanid))
            break
        else:
            heapq.heappush(hq,humanid)
    if hq:
        humanid=heapq.heappop(hq)
        eat[humanid]+=w
        heapq.heappush(backing,(t+s,humanid))
for i in eat:
    print(i)
            
        
    
    
