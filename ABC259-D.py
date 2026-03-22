from collections import deque
n=int(input())
sx,sy,tx,ty=map(int,input().split())
circles=[]
for i in range(n):
    x,y,r=map(int,input().split())
    circles.append((x,y,r))
nodes=[[] for _ in range(n)]
for i in range(n):
    if (circles[i][0]-sx)**2+(circles[i][1]-sy)**2==circles[i][2]**2:
        start=i
    #print((circles[i][0]-tx)**2,(circles[i][1]-ty)**2,circles[i][2]**2)
    if (circles[i][0]-tx)**2+(circles[i][1]-ty)**2==circles[i][2]**2:
        goal=i 
    for k in range(i+1,n):
        if (circles[i][0]-circles[k][0])**2+(circles[i][1]-circles[k][1])**2<=(circles[i][2]+circles[k][2])**2 and ((circles[i][0]-circles[k][0])**2+(circles[i][1]-circles[k][1])**2>=(max(circles[i][2],circles[k][2])-min(circles[i][2],circles[k][2]))**2):
            nodes[i].append(k)
            nodes[k].append(i)
#print(nodes)
#print(start)
# print(goal)
q=deque()
q.append(start)
visited=[False]*(n+1)
while q:
    nxt=q.popleft()
    if nxt == goal:
        print("Yes")
        exit()
    for point in nodes[nxt]:
        if visited[point]==False:
            visited[point]=True
            q.append(point)
print("No")
            
            