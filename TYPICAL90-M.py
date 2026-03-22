import heapq
n,m=map(int,input().split())
costfromone=[10**18]*(n+1)
costfromzero=[10**18]*(n+1)
nodes=[[]for _ in range(n+1)]
for i in range(m):
    a,b,c=map(int,input().split())
    nodes[a].append((b,c))
    nodes[b].append((a,c))
hq=[]
heapq.heappush(hq,(0,1))
costfromone=[10**18]*(n+1)
costfromone[1]=0
#print(nodes)
fromone=set()
while hq:
    #print(hq)
    cost,point=heapq.heappop(hq)
    fromone.add(point)
    if len(fromone)==n:
        break
    for i,cost in nodes[point]:
        if costfromone[i]>costfromone[point]+cost:
            costfromone[i]=costfromone[point]+cost
            heapq.heappush(hq,(costfromone[point]+cost,i))
#print(costfromone)
hq=[]
heapq.heappush(hq,(0,n))
costfromzero=[10**18]*(n+1)
costfromzero[n]=0
fromzero=set()
#print(nodes)
while hq:
    #print(hq)
    cost,point=heapq.heappop(hq)
    fromzero.add(point)
    if len(fromzero)==n:
        break
    for i,cost in nodes[point]:
        if costfromzero[i]>costfromzero[point]+cost:
            costfromzero[i]=costfromzero[point]+cost
            heapq.heappush(hq,(costfromzero[point]+cost,i))
for i in range(1,n+1):
    print(costfromzero[i]+costfromone[i])