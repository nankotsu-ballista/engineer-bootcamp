import heapq
n,q=map(int,input().split())
hq=[]
for i in range(n):
    heapq.heappush(hq,i+1)
#print(hq)
called=[]
calledset=set()
for i in range(q):
    event=list(map(int,input().split()))
    if event[0]==1:
        humanid=heapq.heappop(hq)
        heapq.heappush(called,humanid)
        calledset.add(humanid)
        #print(humanid)
    elif event[0]==2:
        calledset.discard(event[1])
    elif event[0]==3:
        while True:
            humanid=heapq.heappop(called)
            if humanid in calledset:
                break
        heapq.heappush(called,humanid)
        print(humanid)