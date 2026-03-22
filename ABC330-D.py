from collections import deque
N=int(input())
grid = [input() for _ in range(N)]
xlist=[0]*N
ylist=[0]*N
for i in range(N):
    for j in range(N):
       if grid[i][j]=="o":
           xlist[j]+=1
           ylist[i]+=1
sum=0
for i in range(N):
    for j in range(N):
        if grid[i][j]=="o" and xlist[j]>= 2 and ylist[i]>= 2:
            sum+=(xlist[j]-1)*(ylist[i]-1)
print(sum)