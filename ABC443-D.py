import heapq
t=int(input())
for _ in range(t):
    n=int(input())
    r=list(map(int,input().split()))
    hq=[]
    for i in range(n):
        heapq.heappush(hq,(r[i],i))
    #print(hq)
    #print(r)
    ans=0
    while hq:
        y,idx=(heapq.heappop(hq))
        if idx+1<n and r[idx+1]>=y+2:
            ans+=r[idx+1]-(y+1)
            r[idx+1]=y+1
            heapq.heappush(hq,(r[idx+1],idx+1))
        if 0<=idx-1 and r[idx-1]>=y+2:
            ans+=r[idx-1]-(y+1)
            r[idx-1]=y+1
            heapq.heappush(hq,(r[idx-1],idx-1))
    print(ans)
        
    
