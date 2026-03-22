from collections import deque
n,m=map(int,input().split())
p=list(map(int,input().split()))
p=[0]+p
childs=[[] for _ in range(n+1)]
for i in range(1,n):
    childs[p[i]].append(i+1)
#print(childs)
maxlayers=[-1]*(n+1)
for i in range(m):
    x,y=map(int,input().split())
    if maxlayers[x] < y:
        maxlayers[x]=y
q=deque()
q.append(1)
#print(maxlayers)
while q:
    #print(q)
    point=q.popleft()
    layers=maxlayers[point]
    for child in childs[point]:
        if maxlayers[child]<layers-1:
            maxlayers[child]=layers-1
        q.append(child)
#print(maxlayers)
ans=0
for i in maxlayers:
    if i>=0:
        ans+=1
print(ans)