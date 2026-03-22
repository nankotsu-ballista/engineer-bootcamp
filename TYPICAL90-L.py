import bisect
h,w=map(int,input().split())
qq=int(input())
n=h*w
def find(x):
    while parent[x] != x:
        parent[x] = parent[parent[x]]
        x = parent[x]
    return x

def union(a, b):
    ra, rb = find(a), find(b)
    if ra == rb: 
        return
    if size[ra] < size[rb]:
        ra, rb = rb, ra
    parent[rb] = ra
    size[ra] += size[rb]
parent=[]
size=[]
grid=[[False]*w for _ in range(h)]
di=[1,-1,0,0]
dk=[0,0,1,-1]
for i in range(n+1):
    parent.append(i)
    size.append(1)
for i in range(qq):
    q=list(map(int,input().split()))
    num=q[0]
    if num==1:
        r=q[1]-1
        c=q[2]-1
        grid[r][c]=True
        for d in range(4):
            ni=di[d]+r
            nk=dk[d]+c
            if -1<ni<h and -1<nk<w:
                if grid[ni][nk]==True:
                    #print(ni*w+nk,r*w+c)
                    union(ni*w+nk,r*w+c)
    elif num==2:
        ra=q[1]-1
        ca=q[2]-1
        rb=q[3]-1
        cb=q[4]-1
        if find(rb*w+cb) == find(ra*w+ca) and grid[rb][cb]==True and grid[ra][ca]==True:
            print("Yes")
        else:
            print("No")
# for i in grid:
#     print(i)
# for i in range(h):
#     for k in range(w):
#         print([i,k],find(i*w+k))