from collections import deque
q=deque()
q.append((0,0))
h,w=map(int,input().split())
grid=[list(map(str,input().strip())) for _ in range(h)]
#print(grid)
s=set()
ans=0
while q:
    i,k=q.popleft()
    ans=max(ans,i+k)
    if i+1<h and (i+1,k) not in s and grid[i+1][k]==".":
        s.add((i+1,k))
        q.append((i+1,k))
    if k+1<w and (i,k+1) not in s and grid[i][k+1]==".":
        s.add((i,k+1))
        q.append((i,k+1))
print(ans+1)