from collections import deque
n,m=map(int,input().split())
nodes=[[] for _ in range(n+1)]
for i in range(m):
    y,x=map(int,input().split())
    nodes[x].append(y)
q=int(input())
points=[False]*(n+1)
# print(points)
# print(q)
for i in range(q):
    knd,v=map(int,input().split())
    if knd==1:
        if points[v]==False:
            points[v]=True
            que=deque()
            que.append(v)
            while que:
                cc=que.popleft()
                for c in nodes[cc]:
                    if points[c]==False:
                        points[c]=True
                        que.append(c)
        #print(points)
                
                
    elif knd==2:
        if points[v]==True:
            print("Yes")
        else:
            print("No")
    
    
    