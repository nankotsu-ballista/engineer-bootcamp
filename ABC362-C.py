N=int(input())
minsum=0
maxsum=0
kyori=[0]*N
ans=[0]*N
for i in range(N):
    L,R=map(int,input().split())
    ans[i]=L
    minsum +=L
    maxsum +=R
    kyori[i]=R-L
#print(minsum)
#print(maxsum)
if minsum<=0 and maxsum>=0:
    print("Yes")
else:
    print("No")
    exit()
umeru=0-minsum
#print(ans)
found=False
for i in range(N):
    if kyori[i] >= umeru:
        ans[i] += umeru
        found=True
    else:
        ans[i] +=kyori[i]
        umeru-=kyori[i]
    if found==True:
        break
print(*ans)