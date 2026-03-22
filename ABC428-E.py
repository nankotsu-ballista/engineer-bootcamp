from collections import deque
n=int(input())
nodes=[[] for _ in range(n+1)]
q=deque()
for i in range(n-1):
    a,b=map(int,input().split())
    nodes[a].append(b)
    nodes[b].append(a)
visited=[-1]*(n+1)
visited[a]=0
q.append(a)
while q:
    idx=q.pop()
    for point in nodes[idx]:
        if visited[point]==-1:
            visited[point]=visited[idx]+1
            q.append(point)
value=max(visited)
for i in range(n,-1,-1):
    if value==visited[i]:
        minidx=i
        minvalue=value
        break
q=deque()
visited=[-1]*(n+1)
visited[minidx]=0
q.append(minidx)
while q:
    idx=q.pop()
    for point in nodes[idx]:
        if visited[point]==-1:
            visited[point]=visited[idx]+1
            q.append(point)
value=max(visited)
for i in range(n,-1,-1):
    if value==visited[i]:
        maxidx=i
        maxvalue=value
        break








maxvisited=[-1]*(n+1)
q.append(maxidx)
maxvisited[maxidx]=0
while q:
    idx=q.pop()
    for point in nodes[idx]:
        if maxvisited[point]==-1:
            maxvisited[point]=maxvisited[idx]+1
            q.append(point)
# print(maxvisited)
# print(visited)
if minidx>maxidx:
    maxvisited,visited=visited,maxvisited
    minidx,maxidx=maxidx,minidx
# print(maxvisited)
# print(visited)
for i in range(1,n+1):
    if visited[i]>maxvisited[i]:
        print(minidx)
    else:
        print(maxidx)






