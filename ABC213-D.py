from collections import defaultdict,deque
import heapq
import sys
sys.setrecursionlimit(300000)
n=int(input())
nodes=[[] for _ in range(n+1)]
for i in range(n-1):
    a,b=map(int,input().split())
    nodes[a].append(b)
    nodes[b].append(a)
for i in range(1,n+1):
    nodes[i].sort()
visited=[False]*(n+1)
visited[1]=True
trail=[]
def dfs(c):
    trail.append(c)
    for k in nodes[c]:
        if visited[k]==False:
            visited[k]=True
            dfs(k)
            trail.append(c)
dfs(1)
print(*trail)
            
        
        