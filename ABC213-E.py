from collections import defaultdict,deque
import heapq
h,w=map(int,input().split())
grid = [list(map(str,input().strip())) for _ in range(h)]
di=[0,0,1,-1]
dk=[-1,1,0,0]
ddi=[2,2,2,-2,-2,-2,  1,1,1,1,1 ,-1,-1,-1,-1,-1  ,0,0,0,0]
ddk=[1,-1,0,1,-1,0,   0,-1,1,2,-2 ,0,-1,1,2,-2  ,1,-1,2,-2  ]
visited=[[10**18]*w for _ in range(h)]
hq=[]
heapq.heappush(hq,(0,0,0))
visited[0][0]=0
while hq:
    #print(hq)
    cost,i,k=heapq.heappop(hq)
    if i==h-1 and k ==w-1:
        print(cost)
        #print(visited)
        exit()
    for d in range(4):
        ni=i+di[d]
        nk=k+dk[d]
        if -1<ni<h and -1<nk<w:
            if grid[ni][nk]=="." and visited[ni][nk]>cost:
                heapq.heappush(hq,(cost,ni,nk))
                visited[ni][nk]=cost
    for dd in range(20):
        ni=i+ddi[dd]
        nk=k+ddk[dd]
        if -1<ni<h and -1<nk<w:
            if visited[ni][nk]>cost+1:
                heapq.heappush(hq,(cost+1,ni,nk))
                visited[ni][nk]=cost+1

                
    
    