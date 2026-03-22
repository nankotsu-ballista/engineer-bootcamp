from collections import deque
n=int(input())
zeroone=[-1]*(n+1)
nodes=[[] for _ in range(n+1)]
for i in range(n-1):
    a,b=map(int,input().split())
    nodes[a].append(b)
    nodes[b].append(a)
q=deque()
q.append((1,1))
zeroone[1]=1
while q:
    #print(q)
    point,zo=q.popleft()
    if zo==1:
        nxtzo=0
    else:
        nxtzo=1
    for i in nodes[point]:
        if zeroone[i]==-1:
            zeroone[i]=nxtzo
            q.append((i,nxtzo))
#print(zeroone)
one=0
zero=0
for i in range(1,n+1):
    if zeroone[i]==1:
        one+=1
    else:
        zero+=1
cny=0
ans=[]
if one>zero:
    for i in range(1,n+1):
        if cny>=n//2:
            break
        if zeroone[i]==1:
            cny+=1
            ans.append(i)
else:
    for i in range(1,n+1):
        if cny>=n//2:
            break
        if zeroone[i]==0:
            cny+=1
            ans.append(i)
print(*ans)
    
