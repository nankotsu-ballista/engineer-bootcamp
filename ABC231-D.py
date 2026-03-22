from functools import lru_cache
import math,bisect,heapq
from collections import deque
n,m=map(int,input().split())
tonari=[[]for _ in range(n+1)]
dfs=[[]for _ in range(n+1)]
for i in range(m):
    a,b=map(int,input().split())
    tonari[a].append(b)
    tonari[b].append(a)
    if len(dfs[a])==0:
        dfs[a].append(b)
    else:
        dfs[b].append(a)
#print(tonari)


#print(dfs)
check=False
for i in range(1,n+1):
    if len(tonari[i])!=2:
        check=True
    if len(tonari[i])>2:
        print("No")
        exit()
visited=[False]*(n+1)
for i in range(1,n+1):
    if len(tonari[i])!=0 and visited[i]==False:
        q=deque()
        q.append((i,-1))
        visited[i]=True
        while q:
            #print(q)
            tmp,oya=q.popleft()
            visited[tmp]=True
            for i in tonari[tmp]:
                if i!=oya:
                    if visited[i]==True:
                        print("No")
                        exit()
                    else:
                        q.append((i,tmp))
                    
            
print("Yes")
            
    