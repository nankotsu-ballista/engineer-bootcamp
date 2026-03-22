import heapq
n,m=map(int,input().split())
s=[set() for _ in range(n+1)]
tokihanate=[set() for _ in range(n+1)]
for i in range(m):
    a,b=map(int,input().split())
    s[b].add(a)
    tokihanate[a].add(b)
ans=[]
#print(s)
q=[]
for i in range(1,n+1):
    if len(s[i])==0:
        heapq.heappush(q,i)
#print(q)
while q:
    #print(q)
    nxt=heapq.heappop(q)
    ans.append(nxt)
    for k in tokihanate[nxt]:
        check=False
        if len(s[k])==1:
            check=True
        s[k].discard(nxt)
        if len(s[k])==0 and check==True:
            heapq.heappush(q,k)
            

if len(ans)==n:
    print(*ans)
else:
    print(-1)