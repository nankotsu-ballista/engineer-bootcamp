from collections import deque
n,m=map(int,input().split())
nodes=[[] for _ in range(n+1)]
s=set()
for i in range(m):
    x,y=map(int,input().split())
    s.add((x,y))
s=list(s)
count=[0]*(n+1)
for x,y in s:
    nodes[y].append(x)
    count[x]+=1
q=deque()
#print(count)
for i in range(1,n+1):
    if count[i]==0:
        q.append(i)
ans=[-1]*(n+1)
newq=[]
#print(nodes)
while q:
    #print(q)
    if len(q)!=1:
        print("No")
        exit()
    point=q.popleft()
    newq.append(point)
    for i in nodes[point]:
        count[i]-=1
        if count[i]==0:
            q.append(i)
print("Yes")
newq=list(newq)
newq.reverse()
for i in range(len(newq)):
    ans[newq[i]]=i+1
    
print(*ans[1:])
