from collections import deque
n=int(input())
s=set()
nodes=[[] for _ in range(n+1)]
for i in range(n):
    CP=list(map(int,input().split()))
    C=CP[0]
    if C != 0:
        P=CP[1:]
        for k in range(len(P)):
            nodes[i+1].append(P[k])
shouldread=[]
q=deque()
q.append(1)
s.add(1)
while q:
    node=q.pop()
    for i in nodes[node]:
        if i not in s:
            s.add(i)
            q.append(i)
c=s
s=list(s)
nodecount=[0]*(n+1)
gyakunode=[[]for _ in range(n+1)]
for i in s:
    nodecount[i]=len(nodes[i]) 
    if nodecount[i]==0 and i in c:
        q.append(i)
    for k in nodes[i]:
        gyakunode[k].append(i)

while q:
    t=q.popleft()
    shouldread.append(t)
    for i in gyakunode[t]:
        nodecount[i]-=1
        if nodecount[i]==0:
            q.append(i)
ans=shouldread[:-1]
print(*ans)
    
    