import heapq
hq = []
n= int(input())
info=[list(map(int,input().split())) for _ in range(n-1)]
heapq.heappush(hq,(0,1))
dist=[10**18]*(n+1)
while hq:
    cost,stage = heapq.heappop(hq)
    if stage == n:
        print(cost)
        exit()
    if dist[stage+1]>cost+info[stage-1][0]:
        heapq.heappush(hq,(cost+info[stage-1][0],stage+1))
        dist[stage+1]=cost+info[stage-1][0]
    if dist[info[stage-1][2]]>cost+info[stage-1][1]:
        heapq.heappush(hq,(cost+info[stage-1][1],info[stage-1][2]))
        dist[info[stage-1][2]]=cost+info[stage-1][1]