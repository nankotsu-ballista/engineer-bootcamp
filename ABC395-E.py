import heapq
N,M,X=map(int,input().split())
cost=[[10**18]*2 for _ in range(N+1)]
h=[]
nodes=[[]for _ in range(N+1)]
revnodes=[[]for _ in range(N+1)]
for i in range(M):
    u,v=map(int,input().split())
    nodes[u].append(v)
    revnodes[v].append(u)
# print(nodes)
# print(revnodes)
heapq.heappush(h,(0,1,0))
cost[1][0]=0
while h:
    #print(h)
    Acost,x,switch = heapq.heappop(h)
    if x==N:
        #print(Acost,x,switch)
        print(Acost)
        exit()
    if switch==0:
        for i in (nodes[x]):
            if cost[i][switch]>cost[x][switch]+1:
                cost[i][switch]=cost[x][switch]+1
                heapq.heappush(h,(cost[i][switch],i,switch))
        if cost[x][1]>cost[x][0]+X:
            cost[x][1]=cost[x][0]+X
            heapq.heappush(h,(cost[x][0]+X,x,1))
        
    elif switch==1:
        for i in (revnodes[x]):
            if cost[i][switch]>cost[x][switch]+1:
                cost[i][switch]=cost[x][switch]+1
                heapq.heappush(h,(cost[i][switch],i,switch))
        if cost[x][0]>cost[x][1]+X:
            cost[x][0]=cost[x][1]+X
            heapq.heappush(h,(cost[x][1]+X,x,0))
print(cost)
        
        
            