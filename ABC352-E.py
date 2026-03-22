import heapq
n,m=map(int,input().split())
hq=[]
s=set()
minc=10**18
for i in range(m):
    k,c=map(int,input().split())
    A=list(map(int,input().split()))
    heapq.heappush(hq,(c,A))
    minc=min(minc,c)
count=0
cost=0
parent=[]
size=[]
for i in range(n+1):
    parent.append(i)
for i in range(n+1):
    size.append(1)
def find(x):
    while parent[x] != x:
        parent[x] = parent[parent[x]]
        x = parent[x]
    return x
#print(size)
#print(parent)
while hq:
    if count==n:
        break
    cos,A=heapq.heappop(hq)
    #print(cos,A)
    initial=A[0]
    for i in A:
        if i == A[0]:
            continue
        if find(A[0])!=find(i):
            la,ra=find(A[0]),find(i)
            if size[la]<size[ra]:
                la,ra=ra,la
            parent[ra]=la
            size[la]+=size[ra]
            count+=1
            cost+=cos
#print(size)
#print(parent)           
if count==n-1:
    print(cost)
else:
    print(-1)
    
