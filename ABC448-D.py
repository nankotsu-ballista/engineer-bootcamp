from collections import deque,defaultdict
import sys
sys.setrecursionlimit(2*10**5+2)
n=int(input())
A=[0]+list(map(int,input().split()))
nodes=[[] for _ in range(n+1)]
comefrom=[-1]*(n+1)
for i in range(n-1):
    u,v=map(int,input().split())
    nodes[u].append(v)
    nodes[v].append(u)
q=deque()
# q.append(1)
# while q:
#     idx=q.popleft()
#     for i in nodes[idx]:
#         if comefrom[i]==-1:
#             q.append(i)
#             comefrom[i]
s=set()
checks=[False]*(n+1)
visited=[False]*(n+1)
count=defaultdict(int)
def dfs(i,check):
    #print(s,i,count)
    if check==True:
        checks[i]=True
    if A[i] in s:
        checks[i]=True
        check=True
    count[A[i]]+=1
    s.add(A[i])
    for k in nodes[i]:
        if visited[k]==False:
            visited[k]=True
            dfs(k,check)
            count[A[k]]-=1
            if count[A[k]]==0:
                s.discard(A[k])
visited[1]=True
dfs(1,False)
for i in range(1,n+1):
    if checks[i]:
        print("Yes")
    else:
        print("No")
    
        