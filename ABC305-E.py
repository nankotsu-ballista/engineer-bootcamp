import heapq
hq=[]
n,m,k=map(int,input().split())
nodes=[[] for _ in range(n+1)]
pointcost=[-1]*(n+1)
for i in range(m):
    a,b=map(int,input().split())
    nodes[b].append(a)
    nodes[a].append(b)
for i in range(k):
    p,h=map(int,input().split())
    heapq.heappush(hq,(-h,p))
    pointcost[p]=h
# print(nodes)
# print(hq)
while hq:
    #print(hq)
    health,p=heapq.heappop(hq)
    health=-health
    if health<0:
        break
    for point in nodes[p]:
        if pointcost[point]<health-1:
            pointcost[point]=health-1
            heapq.heappush(hq,(-health+1,point))
    #print(pointcost)
ans=[]
for i in range(n+1):
    if pointcost[i]>=0:
        ans.append(i)
print(len(ans))
print(*ans)