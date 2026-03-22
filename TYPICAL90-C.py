n,p,kk=map(int,input().split())
A=[list(map(int,input().split())) for _ in range(n)]
dist=[[0]*n for _ in range(n)]
left=0

def calc(X):
    for i in range(n):
        for k in range(n):
            if i == k:
                continue
            if A[i][k]==-1:
                dist[i][k]=X
                continue
            dist[i][k]=A[i][k]
    for k in range(n):
        for i in range(n):
            for j in range(n):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    count=0
    for i in range(n):
        for k in range(n):
            if i == k:
                continue
            if dist[i][k]<=p:
                count+=1
    count=count//2
    return count
if calc(10**10) == kk:
    print("Infinity")
    exit()
left=1
right=10**10
while left<right:
    X=(left+right)//2
    cnt=calc(X)
    if cnt>=kk:
        left=X+1
    else:
        right=X
ans1=left+1
left=1
right=10**10
while left<right:
    X=(left+right)//2
    cnt=calc(X)
    if cnt>=kk+1:
        left=X+1
    else:
        right=X
ans2=left+1
print(ans1-ans2)
    