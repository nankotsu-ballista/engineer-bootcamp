import heapq
hq=[]
tmp=[int(x) for x in input().split()]
h,w,y=tmp[0],tmp[1],tmp[2]
grid=[[int(x) for x in input().split()] for _ in range(h)]
for i in range(h):
    grid[i]=[0]+grid[i]+[0]
t=[0]*(w+2)
grid=[t]+grid+[t]
sink=[[False]*(w+2) for _ in range(h+2)]
for i in range(w+2):
    sink[0][i]=True
    sink[h+1][i]=True
    heapq.heappush(hq,(0,0,i))
    heapq.heappush(hq,(0,h+1,i))
for i in range(h+2):
    sink[i][0]=True
    sink[i][w+1]=True
    heapq.heappush(hq,(0,i,0))
    heapq.heappush(hq,(0,i,w+1))
    
dh=[0,0,1,-1]
dw=[1,-1,0,0]
count=(h+2)*(w+2)+4
anss=[]
for i in range(1,y+1):
    while hq:
        depth,nh,nw=heapq.heappop(hq)
        if depth>i:
            heapq.heappush(hq,(depth,nh,nw))
            break
        count-=1
        for d in range(4):
            th=nh+dh[d]
            tw=nw+dw[d]
            if th<0 or th>h+1 or tw<0 or tw>w+1:
                continue
            if sink[th][tw]==False:
                heapq.heappush(hq,(grid[th][tw],th,tw))
                sink[th][tw]=True
    print(count)