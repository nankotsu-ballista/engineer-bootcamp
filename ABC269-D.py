from collections import deque
import math
n=int(input())
ans=0
hexagon=[[False]*2001 for _ in range(2001)]
for i in range(n):
    x,y=map(int,input().split())
    x=x+1000
    y=y+1000
    hexagon[x][y]=True
for i in range(2001):
    for k in range(2001):
        if hexagon[i][k]==True:
            q=deque()
            q.append((i,k))
            #print(ans)
            while q:
                #print(q)
                x,y=q.popleft()
                hexagon[x][y]=False
                if -1<x-1<2001 and -1< y-1 < 2001 and hexagon[x-1][y-1]==True:
                    q.append((x-1,y-1))
                    hexagon[x-1][y-1]=False
                if -1<x-1<2001 and -1< y < 2001 and hexagon[x-1][y]==True:
                    q.append((x-1,y))
                    hexagon[x-1][y]=False
                if -1<x<2001 and -1< y-1 < 2001 and hexagon[x][y-1]==True :
                    q.append((x,y-1))
                    hexagon[x][y-1]=False
                if -1<x<2001 and -1< y+1 < 2001 and hexagon[x][y+1]==True:
                    q.append((x,y+1))
                    hexagon[x][y+1]=False
                if -1<x+1<2001 and -1< y < 2001 and hexagon[x+1][y]==True:
                    q.append((x+1,y))
                    hexagon[x+1][y]=False
                if -1<x+1<2001 and -1< y+1 < 2001 and hexagon[x+1][y+1]==True:
                    q.append((x+1,y+1))
                    hexagon[x+1][y+1]=False
            ans+=1
print(ans)
    