h,w=map(int,input().split())
grid = [list(input()) for _ in range(h)]
imin=2000
imax=-1
jmin=2000
jmax=-1
for i in range(h):
    for j in range(w):
        if grid[i][j]=="#":
            imin=min(imin,i)
            imax=max(imax,i)
            jmin=min(jmin,j)
            jmax=max(jmax,j)
# print(imin)
# print(jmin)
# print(imax)
# print(jmax)
for i in range(imin,imax+1):
    for j in range(jmin,jmax+1):
        #print(j)
        if grid[i][j]==".":
            print("No")
            #print(i)
            exit()
print("Yes")