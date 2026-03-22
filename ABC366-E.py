n,d=map(int,input().split())
Xs=[]
Ys=[]
for i in range(n):
    x,y=map(int,input().split())
    Xs.append(x)
    Ys.append(y)
R=max(abs(max(Xs)),abs(max(Ys)),abs(min(Xs)),abs(min(Ys)))+10**6
F=[]
G=[]
tmp=-R-d
ansx=0
ansy=0
Xs.sort()
for i in range(n):
    ansx+=abs(tmp-Xs[i])
#print(ansx)
i=1
idx=0
rightcount=n
leftcount=0
Xss=[]
Yss=[]
#print(Xs)
check=False
Axs=[]
Ays=[]
if ansx<=d:
    Axs.append(ansx)
    Xss.append((tmp+i,ansx))
while tmp+i<R+d:
    ansx=ansx-rightcount+leftcount
    if ansx<=d:
        Axs.append(ansx)
        Xss.append((tmp+i,ansx))
    #print(tmp+i)
    while idx<n and Xs[idx]==tmp+i:
        leftcount+=1
        rightcount-=1
        idx+=1
    i+=1
#print(Xss)
#print(Axs)
rightcount=n
leftcount=0

Ys.sort()
for i in range(n):
    ansy+=abs(tmp-Ys[i])
#print(ansy)
idx=0
i=1
if ansy<=d:
    Ays.append(ansy)
    Yss.append((tmp+i,ansy))
while tmp+i<R+d:
    ansy=ansy-rightcount+leftcount
    Yss.append((tmp+i,ansy))
    if ansy<=d:
        Ays.append(ansy)
    while idx<n and Ys[idx]==tmp+i:
        leftcount+=1
        rightcount-=1
        idx+=1
    #print(leftcount,rightcount)
    i+=1
Axs.sort()
Ays.sort()
Ays.reverse()
lenx=len(Axs)
leny=len(Ays)
xidx=0
yidx=0
ans=0
while xidx<lenx and yidx<leny:
    if Axs[xidx]+Ays[yidx]<=d:
        ans+=(leny-yidx)
        xidx+=1
    else:
        yidx+=1
print(ans)


























