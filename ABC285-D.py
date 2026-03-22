from collections import defaultdict,deque
n=int(input())
num=defaultdict(str)
node=[]
nodes=[[]for _ in range(n+1)]
for i in range(n):
    s,t=map(str,input().split())
    num[s]=i+1
    node.append((s,t))
visited=[False]*(n+1)
for i in range(n):
    s,t=node[i]
    nodes[num[s]].append(num[t])
#print(nodes)
q=deque()
for i in range(n+1):
    if visited[i]==False:
        q=deque()
        q.append(i)
        while q:
            nxt=q.popleft()
            visited[nxt]=True
            if nodes[nxt] and nodes[nxt][0]!='':
                q.append(nodes[nxt][0])
                if nodes[nxt][0]==i:
                    print("No")
                    exit()
print("Yes")