N=int(input())
grid = [[0 for _ in range(N)] for _ in range(N)]
count=0
x=0
y=0
i=0
while count < N**2:
    dx=[1 ,0 ,-1 ,0]
    dy=[0 ,-1, 0 ,1]
    if 0 <= y+dy[i] <= N-1 and 0 <= x+dx[i] <= N-1 and grid[y+dy[i]][x+dx[i]]==0:
        grid[y+dy[i]][x+dx[i]]=count
        x=x+dx[i]
        y=y+dy[i]
        count +=1
    else:
        if i==3:
            i=0
        else:
            i = i+1
for i in range(N):
    for j in range(N):
        if grid[i][j]==0:
            grid[i][j]="T"
for row in grid:
    print(*row)