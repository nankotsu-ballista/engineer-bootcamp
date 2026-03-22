from collections import deque
h,w=map(int,input().split())
grid= [list(map(int,input().split())) for _ in range(h)]
isum=[]
ksum=[]
for i in range(h):
    sum=0
    for k in range(w):
        sum+=grid[i][k]
    isum.append(sum)
for k in range(w):
    sum=0
    for i in range(h):
        sum+=grid[i][k]
    ksum.append(sum)
# print(isum)
# print(ksum)
othergrid=[[-1]*w for _ in range(h)]
for i in range(h):
    for k in range(w):
        othergrid[i][k]=isum[i]+ksum[k]-grid[i][k]
for i in range(h):
    print(*othergrid[i])