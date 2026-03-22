import heapq
hq=[]
n,a,b,c=map(int,input().split())
nowcost=[[10**18]*(n+1) for _ in range(2)]
nodes=[[] for _ in range(n+1)]
for i in range(n):
    D=list(map(int,input().split()))
    for k in D:
        nodes[i+1].append(k)
#print(nodes)
heapq.heappush(hq,(0,1,0))
while hq:
    #print(hq)
    cost,point,check=heapq.heappop(hq)
    if point==n:
        print(cost)
        exit()
    if check == 1:
        for t in range(n):
            newcost=nodes[point][t]*b+c
            if nowcost[1][t+1]>cost+newcost:
                heapq.heappush(hq,(cost+newcost,t+1,1))
                nowcost[1][t+1]=cost+newcost
    elif check == 0:
        for t in range(n):
            newcost=nodes[point][t]*b+c
            if nowcost[1][t+1]>cost+newcost:
                heapq.heappush(hq,(cost+newcost,t+1,1))
                nowcost[1][t+1]=cost+newcost
        for t in range(n):
            newcost=nodes[point][t]*a
            if nowcost[0][t+1]>cost+newcost:
                heapq.heappush(hq,(cost+newcost,t+1,0))
                nowcost[0][t+1]=cost+newcost
        
print(nowcost[:5])
    