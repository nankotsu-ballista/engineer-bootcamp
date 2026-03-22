from collections import deque
h,w=map(int,input().split())
grid=[list(map(str,input().strip())) for _ in range(h)]
def migi(i,k):
    for c in range(k+1,w):
        if grid[i][c]=="."  or grid[i][c]=="B":
            if c!=k:
                grid[i][c]="B"
        else:
            break
def hidari(i,k):
    for c in range(k-1,-1,-1):
        if grid[i][c]=="."  or grid[i][c]=="B":
            if c!=k:
                grid[i][c]="B"
        else:
            break
def ue(i,k):
    for c in range(i-1,-1,-1):
        if grid[c][k]=="." or  grid[c][k]=="B":
            if c!=i:
                grid[c][k]="B"
        else:
            break
def sita(i,k):
    for c in range(i+1,h):
        if grid[c][k]=="." or  grid[c][k]=="B":
            if c!=i:
                grid[c][k]="B"
        else:
            break

for i in range(h):
    for k in range(w):
        if grid[i][k]==">":
            migi(i,k)
        elif grid[i][k]=="<":
            hidari(i,k)
        elif grid[i][k]=="^":
            ue(i,k)
        elif grid[i][k]=="v":
            sita(i,k)
# for i in grid:
#     print(i)
di=[0,0,1,-1]
dk=[1,-1,0,0]
q=deque()
visited=[[False]*w for _ in range(h)]
for i in range(h):
    for k in range(w):
        if grid[i][k]=="S":
            q.append((i,k,0))
        if grid[i][k]=="G":
            goali=i
            goalk=k
#print(q)
while q:
    #print(q)
    i,k,times=q.popleft()
    if i==goali and k == goalk:
        print(times)
        exit()
    for c in range(4):
        ni=i+di[c]
        nk=k+dk[c]
        if -1<ni<h and -1<nk<w and visited[ni][nk]==False and (grid[ni][nk]=="G" or grid[ni][nk]=="S" or grid[ni][nk]=="."):
            visited[ni][nk]=True
            q.append((ni,nk,times+1))
print(-1)
                
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        