from collections import deque
import heapq
n,m,k=map(int,input().split())
nodes=[[[],[]]for _ in range(n+1)]
for i in range(m):
    u,v,a=map(int,input().split())
    nodes[u][a].append(v)
    nodes[v][a].append(u)
se=list(map(int,input().split()))
s=set()
visited = [[False, False] for _ in range(n+1)]
for i in se:
    s.add(i)
q=[]
heapq.heappush(q,(0,1,False))
while q:
    time,point,switched=heapq.heappop(q)
    if point==n:
        print(time)
        exit()
    if switched==False and visited[point][1]==False and point in s:
        heapq.heappush(q,(time,point,True))
        visited[point][1]=True
    if switched==True and visited[point][0]==False and point in s:
        heapq.heappush(q,(time,point,False))
        visited[point][0]=True
    if switched==True:
        for i in nodes[point][0]:
            if visited[i][1]==False:
                heapq.heappush(q,(time+1,i,switched))
                visited[i][1]=True
    if switched==False:
        for i in nodes[point][1]:
            if visited[i][0]==False:
                heapq.heappush(q,(time+1,i,switched))
                visited[i][0]=True
print(-1)