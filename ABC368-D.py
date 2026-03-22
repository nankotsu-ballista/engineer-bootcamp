from collections import deque
n,k=map(int,input().split())
tree=[[]for _ in range(n+1)]
for i in range(n-1):
    a,b=map(int,input().split())
    tree[a].append(b)
    tree[b].append(a)
    
#print(tree)
v=list(map(int,input().split()))
v=set(v)
q=deque()
jisuu=[0]*(n+1)
#print(jisuu)
for i in range(n+1):
    jisuu[i]=len(tree[i])
    if i in v:
        continue
    if jisuu[i]==1:
        q.append(i)
ans=0
#print(v)
while q:
    #print(q)
    i=q.pop()
    jisuu[i]=0
    for k in tree[i]:
        if k in v:
            continue
        else:
            jisuu[k]-=1
            if jisuu[k]==1:
                q.append(k)
    ans+=1
print(n-ans)
    
    