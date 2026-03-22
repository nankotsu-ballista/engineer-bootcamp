from collections import deque
n,m=map(int,(input().split()))
nodes=[[]for _ in range(n+1)]
for i in range(m):
    u,v=map(int,(input().split()))
    nodes[u].append(v)
    nodes[v].append(u)
rangelists=[[] for _ in range(n+1)]
for tmp in range(1,n+1):
    q=deque()
    visited=[10**5]*(n+1)
    visited[tmp]=0
    q.append(tmp)
    while q:
        c=q.popleft()
        for i in nodes[c]:
            if visited[i]==10**5:
                visited[i]=visited[c]+1
                q.append(i)
    #print(visited)
    rangelists[tmp]=visited
#print(rangelists)
k=int(input())
checkblackwhite=[False]*(n+1)
items=[]
for i in range(k):
    p,d=map(int,(input().split()))
    items.append((p,d))
    for j in range(n+1):
        if rangelists[p][j]<d:
            checkblackwhite[j]=True
#print(checkblackwhite)
for i in range(k):
    p,d=items[i]
    check=False
    for j in range(n+1):
        if rangelists[p][j]==d and checkblackwhite[j]==False:
            check=True
    if check==False:
        print("No")
        exit()
ans=[]
for i in checkblackwhite:
    #print(i)
    if i == False:
        ans.append("1")
    else:
        ans.append("0")
sn=ans[1:]
print("Yes")
print("".join(sn))
