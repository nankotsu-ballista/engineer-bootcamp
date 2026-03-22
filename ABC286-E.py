import heapq
from collections import deque
n=int(input())
A=list(map(int,input().split()))
nodes=[[] for _ in range(n+1)]
for i in range(n):
    s=input()
    s=list(s)
    for k in range(len(s)):
        if s[k]=="Y":
            nodes[i+1].append(k+1)
#print(nodes)
q=int(input())
anslist=[[-1]*(n+1) for _ in range(n+1)]
for u in range(n+1):
    hq=[]
    timecost=[[10**14,-10**14] for _ in range(n+1)]
    timecost[u][1]=0
    timecost[u][0]=0
    heapq.heappush(hq,(0,-A[u-1],u))
    while hq:
        #print(hq)
        time,cost,point=heapq.heappop(hq)
        if anslist[u][point]!=-1:
            continue
        cost=abs(cost)
        if anslist[u][point]==-1:
            anslist[u][point]=(time,cost)
            
        for k in nodes[point]:
            if timecost[k][0]>time+1:
                timecost[k][0]=time+1
                timecost[k][1]=cost+A[k-1]
                heapq.heappush(hq,(time+1,-cost-A[k-1],k))
            elif timecost[k][0]==time+1:
                if timecost[k][1]<cost+A[k-1]:
                    timecost[k][1]=cost+A[k-1]
                    heapq.heappush(hq,(time+1,-cost-A[k-1],k))
for i in range(q):
    u,v=map(int,input().split())
    if anslist[u][v]==-1:
        print("Impossible")
        continue
    print(*anslist[u][v])
#print(timecost)