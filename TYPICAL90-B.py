from collections import deque
import heapq
n=int(input())
C=list(map(str,input().split()))
nodes=[[] for _ in range(n+1)]
for i in range(n-1):
    a,b=map(int,input().split())
    nodes[a].append(b)
    nodes[b].append(a)
pointtier=[-1]*(n+1)
q=deque()
q.append((1,1))
pointtier[1]=1
qq=[]
while q:
    point,tier=q.popleft()
    heapq.heappush(qq,(-(tier+1),point))
    for i in nodes[point]:
        if pointtier[i]==-1:
            pointtier[i]=tier+1
            q.append((i,tier+1))
sortpoint=[]
while qq:
    tier,point=heapq.heappop(qq)
    tier=-tier
    #print(tier,point)
    sortpoint.append(point)
    
    
#print(sortpoint)
visited=[False]*(n+1)
dp=[[-1]*3 for _ in range(n+1)]   
for p in range(n):
    idx=sortpoint[p]
    visited[idx]=True
    check=False
    for i in nodes[idx]:
        if visited[i]==True:
            check=True
    if check==False:
        if C[idx-1]=="a":
            dp[idx][0]=1
            dp[idx][1]=0
            dp[idx][2]=0
        if C[idx-1]=="b":
            dp[idx][0]=0
            dp[idx][1]=1
            dp[idx][2]=0
    else:
        if C[idx-1]=="a":
            ans=1
            for i in nodes[idx]:
                if visited[i]==True:
                    ans=ans*(dp[i][0]+dp[i][2])
            dp[idx][0]=ans
            ans=1
            for i in nodes[idx]:
                if visited[i]==True:
                    ans=ans*(dp[i][0]+dp[i][1]+2*dp[i][2])
            dp[idx][2]=ans-dp[idx][0]
            dp[idx][1]=0
            for f in range(3):
                dp[idx][f]=dp[idx][f]%(10**9+7)
        elif C[idx-1]=="b":
            ans=1
            for i in nodes[idx]:
                if visited[i]==True:
                    ans=ans*(dp[i][1]+dp[i][2])
            dp[idx][1]=ans
            ans=1
            for i in nodes[idx]:
                if visited[i]==True:
                    ans=ans*(dp[i][0]+dp[i][1]+2*dp[i][2])
            dp[idx][2]=ans-dp[idx][1]
            dp[idx][0]=0
            for f in range(3):
                dp[idx][f]=dp[idx][f]%(10**9+7)
print(dp[1][2])
    

















