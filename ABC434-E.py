from collections import defaultdict,deque
n=int(input())
nodes=defaultdict(list)
visited=defaultdict(list)
counts=defaultdict(int)
s=set()
for i in range(n):
    x,r=map(int,input().split())
    nodes[x+r].append(x-r)
    nodes[x-r].append(x+r)
    s.add(x+r)
    s.add(x-r)
    counts[x+r]+=1
    counts[x-r]+=1
#"print(nodes)
s=list(s)
for i in s:
    visited[i]=False
# print(visited)
# print(counts)
q=deque()
ans=0
for i in range(len(s)):
    count=0
    kindcount=0
    if visited[s[i]]==False:
        q.append(s[i])
        count+=counts[s[i]]
        visited[s[i]]=True
        kindcount+=1
    while q:
        idx=q.popleft()
        for nd in nodes[idx]:
            if visited[nd]==False:
                visited[nd]=True
                q.append(nd)
                count+=counts[nd]
                kindcount+=1
    #print(count//2,kindcount)
    ans+=min(count//2,kindcount)
print(ans)
            
            