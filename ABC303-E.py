from collections import deque
from collections import defaultdict
n=int(input())
nodes=defaultdict(set)
for i in range(n-1):
    u,v=map(int,input().split())
    nodes[u].add(v)
    nodes[v].add(u)
#print(nodes)
counters=[0]*(n+1)
q=deque()
for i in range(n+1):
    if len(nodes[i])==1:
        q.append(i)
        break
ans=[]
while q:
    #print(q)
    leaf=q.pop()
    #print(leaf)
    #print(nodes)
    root=nodes[leaf].pop()
    count=0
    #print("root",root)
    for i in nodes[root]:
        nodes[i].discard(root)
        if len(nodes[i])==0:
            count+=1
        elif len(nodes[i])==1:
            c=nodes[i].pop()
            q.append(c)
            nodes[c].discard(i)
            count+=1
    nodes[root].clear()
    ans.append(count)
ans.sort()
print(*ans)
