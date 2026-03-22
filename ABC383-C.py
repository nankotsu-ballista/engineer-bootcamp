from collections import deque
H,W,D=map(int,input().split())
grid=[list(input()) for _ in range(H)]
q=deque()
visited=[[False]*(W)for _ in range(H)]
for i in range(H):
    for j in range(W):
        if grid[i][j]=="H":
            q.append((i,j,D))

while q:
    A=q.popleft()
    if A[0]<0 or H-1<A[0] or A[1]<0 or W-1<A[1] or grid[A[0]][A[1]]=="#" or visited[A[0]][A[1]]==True:
        continue
    visited[A[0]][A[1]]=True
    if grid[A[0]][A[1]]==".":
        grid[A[0]][A[1]]="H"
    if A[2] == 0:
        continue
    i=A[0]
    j=A[1]
    q.append((i,j-1,A[2]-1))
    q.append((i-1,j,A[2]-1))
    q.append((i,j+1,A[2]-1))
    q.append((i+1,j,A[2]-1))
# print(visited)
# print(q)
# print(grid)
count=0
for i in range(H):
    for j in range(W):
        if grid[i][j]=="H":
            count+=1
print(count)